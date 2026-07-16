from django.db import models
from django.conf import settings

class Announcement(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст оголошення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='announcements',
        verbose_name="Автор"
    )
    
    is_pinned = models.BooleanField(default=False, verbose_name="Закріпити вгорі")

    class Meta:
        verbose_name = "Оголошення"
        verbose_name_plural = "Оголошення"
        ordering = ['-is_pinned', '-created_at']  

    def __str__(self):
        return self.title