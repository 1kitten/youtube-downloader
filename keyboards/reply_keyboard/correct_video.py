from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def correct_or_not() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton('👍 Да'), KeyboardButton('👎 Нет'))
    return keyboard
