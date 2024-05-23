from datetime import timedelta
from django.db import models
from config.settings import AUTH_USER_MODEL
from users.models import NULLABLE, User


# Create your models here.
class Habit(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец', related_name='owner')
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.DateTimeField(verbose_name='время')
    action = models.CharField(max_length=100, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE,
                                      verbose_name='связанная приятная привычка')
    period_choices = (
        (1, "раз в день"), (2, "раз в 2 дня"), (3, "раз в 3 дня"), (4, "раз в 4 дня"),
        (5, "раз в 5 дней"), (6, "раз в 6 дней"), (7, "раз в неделю"),
    )
    period = models.CharField(max_length=12, choices=period_choices, default="раз в день", verbose_name='периодичность')
    reward = models.CharField(max_length=100, **NULLABLE, verbose_name='вознаграждение')
    duration = models.DurationField(default=timedelta(minutes=2), verbose_name='время на выполение')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')
    users = models.ManyToManyField(User, blank=True, verbose_name='пользователи', related_name='users')

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ('action',)
