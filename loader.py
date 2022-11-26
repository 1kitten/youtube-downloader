from telebot import TeleBot
from telebot.types import BotCommand
from telebot.storage import StateMemoryStorage
from config.my_config import my_bot_config


storage = StateMemoryStorage()
bot = TeleBot(token=my_bot_config.bot_token, state_storage=storage)


def set_default_commands(bot):
    bot.set_my_commands(
        [BotCommand(*i) for i in my_bot_config.default_commands]
    )
