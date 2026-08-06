from django.test import TestCase
from django.urls import reverse
from .models import Announcement, AnnouncementComment, AnnouncementVote
from django.contrib.auth import get_user_model

User = get_user_model()

class AnnouncementListTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        # Авторизуємо клієнта для проходження LoginRequiredMiddleware
        self.client.login(username='testuser', password='password123')
        
        self.announcement = Announcement.objects.create(
            title='Test Announcement', 
            author=self.user,
            content='Test content'
        )
        AnnouncementComment.objects.create(announcement=self.announcement, author=self.user, content='Comment 1')
        AnnouncementVote.objects.create(announcement=self.announcement, user=self.user, value=1)

    def test_queryset_annotation(self):
        response = self.client.get(reverse('announcements:announcement_list'))
        self.assertEqual(response.status_code, 200)
        announcements = response.context['announcements']
        self.assertTrue(len(announcements) > 0)
        announcement = announcements[0]
        self.assertEqual(announcement.likes_count, 1)
        self.assertEqual(announcement.comments_count, 1)
