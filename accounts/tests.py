from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountsSecurityAndAuthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testacc', 
            email='test@example.com', 
            password='password123'
        )

    def test_login_open_redirect_protection(self):
        login_url = reverse('accounts:login')
        response = self.client.post(login_url, {
            'username': 'test@example.com',
            'password': 'password123',
            'next': 'http://malicious-site.com'
        }, follow=True)
        self.assertRedirects(response, reverse('home'))

    def test_profile_requires_auth(self):
        response = self.client.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 302)
