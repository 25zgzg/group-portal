from django.db import models
from django.conf import settings

class Thread(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва теми")
    description = models.TextField(blank=True, verbose_name="Опис теми")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='threads',
        verbose_name="Автор"
    )

    class Meta:
        verbose_name = "Гілка форуму"
        verbose_name_plural = "гілки форуму"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Post(models.Model):
    thread = models.ForeignKey(
        Thread, 
        on_delete=models.CASCADE, 
        related_name='posts',
        verbose_name="Тема форуму"
    )
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='posts',
        verbose_name="Автор"
    )
    content = models.TextField(verbose_name="Текст повідомлення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата відправки")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редагування")

    class Meta:
        verbose_name = "Повідомлення форуму"
        verbose_name_plural = "Повідомлення форуму"
        ordering = ['created_at']

    def __str__(self):
        return f"Повідомлення від {self.author.username} в темі {self.thread.title}"