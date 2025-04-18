# users/urls.py
from django.urls import path
from .views import RegisterView, VerifyEmailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RequestPasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('request-password-reset/', RequestPasswordResetView.as_view(), name='request-password-reset'),
    path('reset-password/', PasswordResetConfirmView.as_view(), name='reset-password'),

]