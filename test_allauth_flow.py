import os
import django
from django.http import HttpRequest
from allauth.socialaccount.models import SocialLogin, SocialAccount, EmailAddress
from allauth.socialaccount.internal.flows.signup import process_signup
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_portal.settings')
django.setup()

request = HttpRequest()
request.session = {}

User = get_user_model()
user = User(email='test.google.user@gmail.com')
sociallogin = SocialLogin(user=user)
sociallogin.account = SocialAccount(provider='google', uid='987654321')
sociallogin.email_addresses = [EmailAddress(email='test.google.user@gmail.com', verified=True, primary=True)]

print("--- ТЕСТУВАННЯ process_signup з SOCIALACCOUNT_AUTO_SIGNUP = True ---")
try:
    resp = process_signup(request, sociallogin)
    print(f"Результат виконання process_signup: {resp}")
    print(f"Створений користувач в БД? username={user.username}, pk={user.pk}")
except Exception as e:
    print(f"Помилка: {e}")
