from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import ProfileView, UserCreateView, UserLoginView, SendEmailVerificationCodeView, \
    CheckEmailVerificationCodeView

urlpatterns = [
    path("auth/register/", UserCreateView.as_view(), name="register"),
    path("auth/login/", UserLoginView.as_view(), name="login"),
    path("send/verifycation-code/", SendEmailVerificationCodeView.as_view(), name="send-code"),
    path("email/check-verification/", CheckEmailVerificationCodeView.as_view(), name="check-email-code"),
    path("auth/profile/", ProfileView.as_view(), name="profile"),
]
