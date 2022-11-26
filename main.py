from loader import bot, set_default_commands
from telebot.custom_filters import StateFilter
import handlers


if __name__ == '__main__':
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    bot.infinity_polling()
