from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError



class AuthTest(TestCase):
    def test_password_encryption(self):
        test_user = User.objects.create_user(username='testbot', password='121313145')
        self.assertNotEqual(test_user.password, '121313145')

    def test_logic(self):
            self.assertEqual(1 + 1, 2)
    def test_empty_username_error(self):
            with self.assertRaises(ValueError):
                User.objects.create_user(username=None, password='121313145')

    def test_duplicate_user(self):
            User.objects.create_user(username='testbot', password='password12') 
            with self.assertRaises(IntegrityError):
                User.objects.create_user(username='testbot', password='password13')
    def test_password_check(self):
            test_user = User.objects.create_user(username='testbot', password="password15")
            self.assertTrue(test_user.check_password('password15'))
            self.assertFalse(test_user.check_password('password17'))
