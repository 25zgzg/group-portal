from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from forum.models import Thread
from announcements.models import Announcement

User = get_user_model()

class ModerationTest(TestCase):
    def setUp(self):
        # Створюємо суперюзера (модератора) та звичайного користувача
        self.admin = User.objects.create_superuser(username='admin', password='***', email='admin@test.com')
        self.user = User.objects.create_user(username='user', password='***')
        
        self.thread = Thread.objects.create(title='Thread to delete', creator=self.user)
        self.announcement = Announcement.objects.create(title='Announce to delete', author=self.admin, content='Text')

    def test_moderator_can_delete_thread(self):
        self.client.login(username='admin', password='***')
        response = self.client.post(reverse('moderation:delete_thread', kwargs={'pk': self.thread.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Thread.objects.filter(pk=self.thread.pk).exists())

    def test_regular_user_cannot_access_moderation(self):
        self.client.login(username='user', password='***')
        response = self.client.get(reverse('moderation:dashboard'))
        # Має бути редирект або 403 (залежить від налаштувань middleware/decorators)
        self.assertNotEqual(response.status_code, 200)
