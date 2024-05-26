from config import settings
import requests
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Введите ваш токен сюда
BOT_TOKEN = "your_token_here"

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет! Я твой бот, созданный для работы с API Telegram на Python!')


def echo(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(f'Ты написал: {text}')


def send_telegram_message(chat_id, message):
    params = {
        'text': message,
        'chat_id': chat_id
    }
    response = requests.get(f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage', params=params)


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & amp;
    ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()