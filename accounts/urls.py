from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.contrib.auth.views import LoginView as AuthLoginView

from . import views
from .forms import LoginForm
from .views import ProfileView, LoginView as ApiLoginView

app_name = 'accounts'

urlpatterns = [
    # URLs for standard auth
    path('login/', AuthLoginView.as_view(authentication_form=LoginForm), name='login'),
    # URLs for API auth
    path("api/login/", ApiLoginView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", ProfileView.as_view(), name="profile"),
]