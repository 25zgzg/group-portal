from django.db import models
from django.conf import settings

class Thread(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва теми")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='threads',
        verbose_name="Автор"
    )

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Теми"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Тема"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Автор"
    )
    content = models.TextField(verbose_name="Зміст повідомлення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата відправки")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редагування")

    @property
    def likes_count(self):
        return self.votes.filter(value=1).count()

    @property
    def dislikes_count(self):
        return self.votes.filter(value=-1).count()

    class Meta:
        verbose_name = "Повідомлення"
        verbose_name_plural = "Повідомлення"
        ordering = ['created_at']

    def __str__(self):
        return f"Пост від {self.author} у {self.thread}"

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')
    is_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Зображення поста"
        verbose_name_plural = "Зображення постів"

class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1, 'Like'), (-1, 'Dislike')])

    class Meta:
        unique_together = ('post', 'user')
        verbose_name = "Голос"
        verbose_name_plural = "Голоси"
