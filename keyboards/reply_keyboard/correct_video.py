from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def correct_or_not() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton('๐ ะะฐ'), KeyboardButton('๐ ะะตั'))
    return keyboard
