from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_task",
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовка"
    )
    
    description = models.TextField(
        max_length="100", 
        verbose_name="Описание"
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Выполнена"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создана"
    )
    image = models.ImageField(
        upload_to="image/",
        verbose_name="Фотография"
    )
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ToDo_List"
        verbose_name_plural = "ToDo_Lists"