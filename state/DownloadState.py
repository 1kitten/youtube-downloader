from telebot.handler_backends import State, StatesGroup


class DownloadState(StatesGroup):
    video_link = State()
    correct_video = State()
