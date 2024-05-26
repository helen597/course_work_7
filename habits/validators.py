from datetime import timedelta
from rest_framework import serializers


class DurationValidator:
    """Время выполнения должно быть не больше 120 секунд."""

    def __call__(self, value):
        if value > timedelta(minutes=2):
            raise serializers.ValidationError("Время на выполнение не должно превышать 120 секунд")


class PeriodValidator:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней"""

    def __call__(self, value):
        if not 1 <= value <= 10080:
            raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')


class PleasantHabitValidator:
    """У приятной привычки не может быть вознаграждения или связанной привычки"""

    def __call__(self, value):
        if value['is_pleasant'] and (value['reward'] or value['related_habit']):
            raise serializers.ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")


class PleasantHabitOrRewardValidator:
    """Исключение одновременного выбора связанной привычки и указания вознаграждения"""

    def __call__(self, value):
        if value['reward'] and value['related_habit']:
            raise serializers.ValidationError(
                "У полезной привычки не может быть вознаграждения и связанной привычки одновременно")


class RelatedHabitValidator:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки"""

    def __call__(self, value):
        if value['related_habit']:
            if not value['related_habit'].is_pleasant:
                raise serializers.ValidationError(
                    "В связанные привычки могут попадать только привычки с признаком приятной привычки")
