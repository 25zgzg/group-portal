from django.urls import path
from django.contrib.auth.views import LoginView

from . import views
from .forms import LoginForm


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('register/', views.register, name='register'),
]