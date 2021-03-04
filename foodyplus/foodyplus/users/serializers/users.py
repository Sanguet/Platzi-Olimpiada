# Django
from django.conf import settings
from django.contrib.auth import authenticate
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Tasks
from foodyplus.taskapp.tasks import send_reset_password_email

# Models
from foodyplus.users.models import User

# Utilities
from foodyplus.utils.authenticate import get_tokens_for_user
import jwt


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""

        email = serializers.CharField()

        model = User
        fields = (
            'id',
            'username',
            'email', 'account_type',
            'fav_list'
        )
        read_only_fields = (
            'id',
        )

        depth = 1


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.
    Funcionamiento del login de usuario
    """

    email = serializers.CharField(min_length=2)
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError(
                '1001: Error al iniciar sesion, credenciales invalidas o cuenta deshabilitada'
            )
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token = get_tokens_for_user(self.context['user'])
        return self.context['user'], token


class UserSignUpSerializer(serializers.Serializer):
    """User sign up serializer.
    Funcionamiento de la creacion de cuenta y usuario, con sus validadores
    """
    # User
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())])

    # Phone number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = serializers.CharField(validators=[phone_regex])

    def create(self, data):
        """Creacion de la cuenta principal y usuario admin"""
        # User
        user = User.objects.create_user(
            email=data['email'],
            username=data['username'],
            password=data['password'],
            phone_number=data['phone_number']
        )

        return user


class EmailPasswordSerializer(serializers.Serializer):
    """Serializer de email de reset de contraseña."""

    email = serializers.CharField(min_length=8)

    def validate_email(self, data):
        """Validamos que el email exista para un usuario"""
        try:
            user = User.objects.get(email=data)
        except User.DoesNotExist:
            raise serializers.ValidationError('1022: El email indicado no pertenece a ningun usuario')

        self.context['user'] = user
        return data

    def save(self):
        """Update user's verified status."""
        user = self.context['user']
        send_reset_password_email.delay(user_pk=user.pk)

        return user


class ResetPasswordSerializer(serializers.Serializer):
    """Serializer del reseteo de contraseña."""
    token = serializers.CharField()
    new_password = serializers.CharField(min_length=8)
    new_password_confirmation = serializers.CharField(min_length=8)

    def validate_token(self, data):
        """Verify token is valid."""
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('1012: El token expiro')
        except jwt.PyJWTError:
            raise serializers.ValidationError('1010: El token es incorrecto')
        if payload['type'] != 'reset_password':
            raise serializers.ValidationError('1011: El token es de un tipo incorrecto')

        self.context['payload'] = payload
        return data

    def validate(self, data):
        """Validamos las nuevas contraseñas"""
        passw = data['new_password']
        passw_conf = data['new_password_confirmation']

        if passw != passw_conf:
            raise serializers.ValidationError('1020: Las contraseñas no concuerdan')

        self.context['password'] = data['new_password']
        return data

    def save(self):
        """Reseteo de contraseña"""
        # User
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])

        # Cambio de contraseña
        user.set_password(self.context['password'])
        user.save()

        return self.context['password']
