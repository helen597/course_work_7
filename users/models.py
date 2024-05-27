from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    phone = models.CharField(max_length=35, verbose_name="телефон", **NULLABLE)
    telegram_chat_id = models.CharField(
        max_length=50, unique=True, verbose_name="Telegram_chat_id", **NULLABLE
    )
    country = models.CharField(max_length=100,
                               verbose_name="страна", **NULLABLE)
    city = models.CharField(max_length=100, verbose_name="город", **NULLABLE)
    avatar = models.ImageField(upload_to="users/",
                               verbose_name="аватар", **NULLABLE)
    verification_code = models.CharField(
        max_length=10, verbose_name="код верификации", **NULLABLE
    )
    last_login = models.DateTimeField(**NULLABLE,
                                      verbose_name="дата последнего входа")
    is_active = models.BooleanField(default=False, verbose_name="активен")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ("email",)
