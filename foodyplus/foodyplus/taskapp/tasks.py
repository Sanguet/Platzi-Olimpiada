# Django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

# Models
from foodyplus.users.models import User

# Celery
from celery.decorators import task

# Utilities
import jwt
from datetime import timedelta


def gen_verification_token(user, type_token):
    """Genera el token de verificacion"""
    exp_date = timezone.now() + timedelta(days=3)
    payload = {
        "user": user.username,
        "exp": int(exp_date.timestamp()),
        "type": type_token
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token.decode()


@task(name='send_confirmation_email', max_retries=3)
def send_confirmation_email(user_pk, password):
    """Manda el email de confirmacion y el token"""
    user = User.objects.get(pk=user_pk)
    verification_token = gen_verification_token(user=user, type_token='email_confirmation')
    subject = 'Bienvenido @{}, ya estas listo para usar foodyplus!'.format(user.username)
    from_email = 'foodyplus <noreply@switch.com>'
    content = render_to_string(
        'emails/users/account_verification.html',
        {'token': verification_token, 'user': user, 'password': password}
    )
    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, "text/html")
    msg.send()


@task(name='send_reset_password_email', max_retries=3)
def send_reset_password_email(user_pk):
    """Manda el email reset de contraseña y token"""
    user = User.objects.get(pk=user_pk)
    verification_token = gen_verification_token(user=user, type_token='reset_password')
    subject = 'Reseteo de contraseña del usuario {}'.format(user.username)
    from_email = 'foodyplus <noreply@foodyplus.com>'
    content = render_to_string(
        'emails/users/reset_password.html',
        {'token': verification_token, 'user': user}
    )
    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, "text/html")
    msg.send()
