from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Thread, Post, Vote

User = get_user_model()

class ForumTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='forumuser', password='password123')
        self.client.login(username='forumuser', password='password123')
        self.thread = Thread.objects.create(title='Test Thread', creator=self.user)
        self.post = Post.objects.create(thread=self.thread, author=self.user, content='Initial post')

    def test_vote_post(self):
        # Перевіряємо голосування через POST запит
        response = self.client.post(reverse('forum:vote_post', kwargs={'post_pk': self.post.pk}), {'value': 1})
        self.assertEqual(response.status_code, 302) # Редирект назад
        
        self.post.refresh_from_db()
        self.assertEqual(self.post.likes_count, 1)
        self.assertTrue(Vote.objects.filter(post=self.post, user=self.user, value=1).exists())
