import os
import django
import traceback

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_portal.settings')
django.setup()

from allauth.socialaccount.models import SocialLogin
from accounts.adapter import CustomSocialAccountAdapter
from django.contrib.auth import get_user_model

class MockAccount:
    provider = 'google'
    extra_data = {
        'email': 'test.user@gmail.com',
        'name': 'Test User',
        'picture': 'https://example.com/avatar.jpg'
    }

class MockSocialApp:
    provider = 'google'

class MockSocialLogin(SocialLogin):
    def __init__(self):
        self.account = MockAccount()
        self.app = MockSocialApp()
        self.user = get_user_model()()
        self.state = {}
        self.token = None

print("--- ТЕСТУВАННЯ ALLAUTH SOCIAL LOGIN FLOW ---")
sociallogin = MockSocialLogin()
adapter = CustomSocialAccountAdapter()

try:
    # Симулюємо те, що робить allauth у socialaccount/views.py або adapter.is_open_for_signup
    print("Виклик adapter.populate_user...")
    user = adapter.populate_user(None, sociallogin, sociallogin.account.extra_data)
    print(f"Після populate_user -> username: '{user.username}', email: '{user.email}'")
    
    # Перевірка requires_signup або подібної логіки allauth
    print("Перевірка requires_signup...")
    # Allauth перевіряє, чи заповнені обов'язкові поля
    user.full_clean()
except Exception as e:
    print(f"\n[СПІЙМАНО ПОМИЛКУ / ПРИЧИНУ РЕДІРЕКТУ]: {e}")
    traceback.print_exc()
