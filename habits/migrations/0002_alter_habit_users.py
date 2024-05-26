# Generated by Django 5.0.6 on 2024-05-26 10:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='пользователи'),
        ),
    ]
