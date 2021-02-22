# Django
from django.conf import settings
from django.contrib.auth import authenticate

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Tasks
from dummy.taskapp.tasks import send_confirmation_email, send_reset_password_email

# Models
from dummy.users.models import User, Profile

# Utilities
from dummy.utils.authenticate import get_tokens_for_user
import jwt
import random
from string import ascii_uppercase, digits


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""

        model = User
        fields = (
            'id',
            'username',
            'email', 'account_type'
        )
        read_only_fields = (
            'id',
        )

    def create(self, data):
        """Creacion de un usuario por medio de un admin"""
        # Creamos los ultimos datos necesarios para el new_user
        password = SucesionAleatoria()
        username = 'dummy' + str(SucesionAleatoria())

        # Creacion del usuario
        new_user = User.objects.create_user(
            email=data['email'],
            username=username,
            password=password,
            is_verified=False
        )

        # Creamos el perfil y mandamos el email de verificacion
        Profile.objects.create(user=new_user)
        send_confirmation_email.delay(user_pk=new_user.pk, password=password)

        return new_user


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.
    Funcionamiento del login de usuario
    """

    username = serializers.CharField(min_length=2)
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError(
                '1001: Error al iniciar sesion, credenciales invalidas o cuenta deshabilitada'
            )
        if not user.is_verified:
            raise serializers.ValidationError(
                '1002: Error al iniciar sesion, el usuario necesita ser activado'
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

    def create(self, data):
        """Creacion de la cuenta principal y usuario admin"""
        # User
        password = SucesionAleatoria()
        self.context['password'] = password
        username = 'dummy' + str(SucesionAleatoria())
        user = User.objects.create_user(
            email=data['email'],
            username=username,
            password=password,
            is_verified=False
        )
        Profile.objects.create(user=user)
        send_confirmation_email.delay(user_pk=user.pk, password=self.context['password'])

        return user


def SucesionAleatoria():
    CODE_LENGTH = 13
    pool = ascii_uppercase + digits
    code = random.choices(pool, k=CODE_LENGTH)
    code = "".join(code)
    return code


class AccountVerificationSerializer(serializers.Serializer):
    """Account verification serializer."""

    token = serializers.CharField()

    def validate_token(self, data):
        """Verify token is valid."""
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('1012: El token expiro')
        except jwt.PyJWTError:
            raise serializers.ValidationError('1010: El token es incorrecto')
        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('1011: El token es de un tipo incorrecto')

        self.context['payload'] = payload
        return data

    def save(self):
        """Update user's verified status."""
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()


class ChangePasswordSerializer(serializers.Serializer):
    """Serializer del cambio de contraseña."""

    old_password = serializers.CharField()
    new_password = serializers.CharField(min_length=8)
    new_password_confirmation = serializers.CharField(min_length=8)

    def validate_old_password(self, data):
        """Validamos la contraseña vieja/actual"""
        user = self.context['request'].user
        if not user.check_password(data):
            raise serializers.ValidationError('1020: La contraseña que indico no es la correcta')

        return data

    def validate(self, data):
        """Validamos las nuevas contraseñas"""
        passw = data['new_password']
        passw_conf = data['new_password_confirmation']

        if passw != passw_conf:
            raise serializers.ValidationError("1021: Las contraseñas no concuerdan")

        self.context['password'] = data['new_password']
        return data

    def save(self):
        """Update user's verified status."""
        user = self.context['request'].user
        user.set_password(self.context['password'])
        user.save()

        return self.context['password']


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
