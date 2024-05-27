import requests
from config import settings


def send_telegram_message(chat_id, message):
    """Функция отправки уведомления в Telegram"""
    params = {'chat_id': chat_id, 'text': message}
    print(f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}')
    return requests.post(
        f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage',
        params=params
    )
