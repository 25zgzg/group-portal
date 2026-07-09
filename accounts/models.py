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

#TODO: дописати логіку