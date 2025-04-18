from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = AccessToken.for_user(user)
    return str(AccessToken.for_user(user))

def send_verification_email(user):
    token = get_tokens_for_user(user)
    verify_url = f"http://localhost:8001/users/verify-email/?token={token}"

    send_mail(
        subject="Verify your email",
        message=f"Click the link to verify your email: {verify_url}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
    )
