from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_USER = 'user'
    ROLE_MODERATOR = 'moderator'
    ROLE_ADMIN = 'admin'

    ROLE_CHOICES = [
        (ROLE_USER, 'Користувач'),
        (ROLE_MODERATOR, 'Модератор'),
        (ROLE_ADMIN, 'Адміністратор'),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=15,
        choices=ROLE_CHOICES,
        default=ROLE_USER
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    @property
    def is_moderator(self):
        return self.role == self.ROLE_MODERATOR or self.is_superuser

    @property
    def is_administrator(self):
        return self.role == self.ROLE_ADMIN or self.is_superuser

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followed')
        verbose_name = "Підписка"
        verbose_name_plural = "Підписки"
