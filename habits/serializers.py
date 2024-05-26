from rest_framework import serializers
from habits.models import Habit
from habits.validators import (DurationValidator, PleasantHabitValidator,
                               PleasantHabitOrRewardValidator, RelatedHabitValidator, PeriodValidator)


class HabitSerializer(serializers.ModelSerializer):
    duration = serializers.DurationField(validators=[DurationValidator])
    period = serializers.IntegerField(validators=[PeriodValidator])

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [PleasantHabitValidator(), PleasantHabitOrRewardValidator(), RelatedHabitValidator()]
