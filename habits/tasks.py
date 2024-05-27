from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_alert():
    """Функция оповещения о полезной привычке"""
    current_datetime = timezone.now().today().replace(second=0, microsecond=0)
    habits = Habit.objects.filter(is_pleasant=False).filter(time=current_datetime)
    for habit in habits:
        message_1 = f"Полезная привычка: {habit}"
        print(message_1)
        if habit.related_habit:
            message_2 = f"За выполнение Вы можете: {habit.related_habit}"
        elif habit.reward:
            message_3 = f"За выполнение Вам можно: {habit.reward}"

        for user in habit.users.all():
            if user.telegram_chat_id:
                response = send_telegram_message(
                    chat_id=user.telegram_chat_id,
                    message=message_1,
                )
                print(response)
                if habit.related_habit:
                    response = send_telegram_message(
                        chat_id=user.telegram_chat_id,
                        message=message_2,
                    )
                    print(response)
                    # print(message_2)
                elif habit.reward:
                    response = send_telegram_message(
                        chat_id=user.telegram_chat_id,
                        message=message_3,
                    )
                    print(response)
                    # print(message_3)
        habit.time = habit.time + timedelta(minutes=habit.period)
        habit.save()
