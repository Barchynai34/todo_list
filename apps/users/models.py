from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(
        max_length=100,
        verbose_name="Email"
    )
    create_at = models.DateField(
        auto_now_add=True,
        verbose_name="Создано"
    )
    phone_number = models.CharField(
        max_length=200,
        verbose_name="Телефонный номер",
        help_text="Например: +996 (221) 222 222"
    )
    age = models.PositiveIntegerField(
        verbose_name="Возраст",
        help_text="Например: 18",
        blank=True, null=True
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"