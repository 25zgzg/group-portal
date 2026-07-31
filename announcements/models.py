from django.db import models
from django.conf import settings

class Announcement(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Зміст оголошення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='announcements',
        verbose_name="Автор"
    )

    class Meta:
        verbose_name = "Оголошення"
        verbose_name_plural = "Оголошення"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class AnnouncementComment(models.Model):
    announcement = models.ForeignKey(
        Announcement,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Оголошення"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='announcement_comments',
        verbose_name="Автор"
    )
    content = models.TextField(verbose_name="Зміст коментаря")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Коментар до оголошення"
        verbose_name_plural = "Коментарі до оголошень"
        ordering = ['created_at']

    def __str__(self):
        return f"Коментар від {self.author} до {self.announcement}"

class AnnouncementVote(models.Model):
    announcement = models.ForeignKey(
        Announcement,
        on_delete=models.CASCADE,
        related_name='votes',
        verbose_name="Оголошення"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Користувач"
    )
    value = models.IntegerField(choices=[(1, 'Like'), (-1, 'Dislike')], verbose_name="Голос")

    class Meta:
        unique_together = ('announcement', 'user')
        verbose_name = "Голос за оголошення"
        verbose_name_plural = "Голоси за оголошення"

