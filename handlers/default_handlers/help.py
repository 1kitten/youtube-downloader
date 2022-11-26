from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['help'])
def bot_help(message: Message) -> None:
    bot.reply_to(message, '📋 Список доступных команд:\n'
                          '/start - Запустить бота\n'
                          '/download - Загрузить видео с YouTube')
