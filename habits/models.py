from datetime import datetime, timedelta
from django.db import models
from config import settings
from config.settings import AUTH_USER_MODEL
from users.models import NULLABLE, User
from datetime import datetime, timedelta
import pytz

zone = pytz.timezone(settings.TIME_ZONE)
current_datetime = datetime.now(zone)


# Create your models here.
class Habit(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец', related_name='owner')
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.DateTimeField(default=current_datetime, verbose_name='время')
    action = models.CharField(max_length=100, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE,
                                      verbose_name='связанная приятная привычка')
    period = models.PositiveIntegerField(default=1440, verbose_name='периодичность (минут)')
    reward = models.CharField(max_length=100, **NULLABLE, verbose_name='вознаграждение')
    duration = models.DurationField(default=timedelta(minutes=2), verbose_name='время на выполение')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')
    users = models.ManyToManyField(User, verbose_name='пользователи', related_name='users', **NULLABLE)

    def __str__(self):
        return f'{self.action} в {self.time.time} {habit.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ('action',)
