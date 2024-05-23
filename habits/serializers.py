from rest_framework import serializers
from habits.models import Habit
from habits.validators import (DurationValidator, PleasantHabitValidator,
                               PleasantHabitOrRewardValidator, RelatedHabitValidator)


class HabitSerializer(serializers.ModelSerializer):
    duration = serializers.DurationField(validators=[DurationValidator])

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [PleasantHabitValidator(), PleasantHabitOrRewardValidator(), RelatedHabitValidator()]
