import requests
from config import settings


def send_telegram_message(chat_id, message):
    """Функция отправки уведомления в Telegram"""
    params = {"text": message, "chat_id": chat_id}
    return requests.post(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage",
        params=params
    )
