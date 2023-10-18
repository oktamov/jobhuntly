from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import ProfileView, UserCreateView, UserLoginView, UserLogoutView, UserPasswordChangeView

urlpatterns = [
    path("auth/register/", UserCreateView.as_view(), name="register"),
    path("auth/login/", UserLoginView.as_view(), name="login"),
    # path("auth/faceobok/", FacebookSocialAuthView.as_view(), name="facebook_login"),
    # path("auth/google/", GoogleSocialAuthView.as_view(), name="google_login"),
    # path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("auth/password/change", UserPasswordChangeView.as_view(), name="password_change"),
    # path("auth/password/reset/", include("django_rest_passwordreset.urls", namespace="password_reset")),
    # path("auth/logout/", UserLogoutView.as_view(), name="logout"),
    # path("auth/profile/", ProfileView.as_view(), name="profile"),
]
