from rest_framework import generics
from .serializers import RegisterSerializer
from .models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from .utils import send_verification_email
from rest_framework.views import APIView
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_bytes, smart_str
from django.core.mail import send_mail

token_generator = PasswordResetTokenGenerator()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        send_verification_email(user)
        return Response({'msg': 'Check your email for verification link'}, status=201)


class VerifyEmailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = AccessToken(token)
            user_id = payload['user_id']
            user = User.objects.get(id=user_id)
            user.is_email_verified = True
            user.save()
            return Response({'message': 'Email successfully verified'})
        except Exception as e:
            return Response({'error': 'Invalid or expired token'}, status=400)


class RequestPasswordResetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.pk))
            token = token_generator.make_token(user)

            reset_url = f"http://localhost:8081/api/users/reset-password/?uid={uidb64}&token={token}"

            send_mail(
                subject='Password Reset Request',
                message=f'Click the link below to reset your password:\n{reset_url}',
                from_email='noreply@example.com',
                recipient_list=[email],
            )

            return Response({'message': 'Password reset link sent to your email.'})
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist.'}, status=404)


class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        uidb64 = request.query_params.get('uid')
        token = request.query_params.get('token')
        new_password = request.data.get('new_password')

        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)

            if token_generator.check_token(user, token):
                user.set_password(new_password)
                user.save()
                return Response({'message': 'Password successfully reset!'})
            else:
                return Response({'error': 'Invalid or expired token.'}, status=400)

        except Exception:
            return Response({'error': 'Something went wrong.'}, status=400)
