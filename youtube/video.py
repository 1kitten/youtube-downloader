import re
from pytube import YouTube
from telebot.apihelper import ApiTelegramException
from loader import bot
import os
from loguru import logger


def is_link_valid(url: str) -> bool:
    if re.match(r"https://www\.youtube\.com/watch\?.*", url) or re.match(r"https://youtu.be/.*", url):
        video_length = YouTube(url).length / 60
        if video_length > 13:
            return False
        return True
    return False


def get_video_image(url: str) -> str:
    img = YouTube(url).thumbnail_url
    return img


def get_video_title(url: str) -> str:
    title = YouTube(url).title
    return title


def download_video(chat_id: int, user_id: int, video_title: str, url: str) -> None:
    try:
        path = f'media/{user_id}/'
        video_title = ''.join(video_title.split()[:1])
        YouTube(url).streams.filter(resolution='360p').first().download(path, filename=video_title+'.mp4')
        logger.info(f'Video {video_title} was downloaded.')
        with open(f'media/{user_id}/{video_title}.mp4', 'rb') as video:
            bot.send_video(chat_id, video=video, caption='🤙 Видео было успешно сохранено!')
    except FileNotFoundError:
        logger.error('There is a problem with video.')
        bot.send_message(chat_id, '😔 Произошла ошибка во время загрузки видео.')
    finally:
        os.remove(f'media/{user_id}/{video_title}.mp4')
