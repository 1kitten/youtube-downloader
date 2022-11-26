from dotenv import find_dotenv, load_dotenv
from dataclasses import dataclass
import os


if not find_dotenv():
    exit('Отсутствуют переменные окружения в файле .env')
else:
    load_dotenv()


@dataclass(frozen=True)
class BotConfig:
    bot_token: str
    default_commands: tuple


my_bot_config = BotConfig(
    bot_token=os.getenv("BOT_TOKEN"),
    default_commands=(
        ('start', 'Запустить бота'),
        ('help', 'Помощь'),
        ('download', 'Скачать видео')
    )
)

