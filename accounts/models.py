from django.contrib.auth.models import AbstractUser
from django.db import models 

class User(AbstractUser):
    class Roles(models.TextChoices):
        STUDENT = 'student', 'Учень'
        MODERATOR = 'moderator', 'Модератор'
        ADMIN =  'admin', 'Адміністратор'

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.STUDENT,
        verbose_name="Роль"
    )

    avatar = models.FileField(upload_to='avatars/', blank=True, null=True, verbose_name="Аватарка")
    bio = models.TextField(max_length=500, blank=True, verbose_name="Про себе")

    def is_moderator(self):
        return self.role == self.Roles.MODERATOR or self.is_staff

    def is_admin(self):
        return self.role == self.Roles.ADMIN or self.is_superuser

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"