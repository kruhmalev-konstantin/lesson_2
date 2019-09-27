# Импортируем нужные библеотеки

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from bot_settings import apikey
import logging


PROXY = {'proxy_url': 'socks5h://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    logging.info(user_text)
    update.message.reply_text(user_text)

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота

def main():
    botapikey = apikey()
    mybot = Updater(botapikey, request_kwargs=PROXY)

    logging.info('Бот запускается! ')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()