from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['start'])
def bot_start(message: Message) -> None:
    bot.reply_to(message, f'Спасибо что запустил 😉 {message.from_user.full_name}\n'
                          f'Список команд доступен по команде /help')
