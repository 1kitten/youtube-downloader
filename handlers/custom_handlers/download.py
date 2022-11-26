from telebot.types import Message
from loader import bot
from state.DownloadState import DownloadState
from youtube.video import get_video_image, get_video_title, download_video
from youtube.video import is_link_valid


@bot.message_handler(commands=['download'])
def bot_download(message: Message) -> None:
    bot.set_state(message.from_user.id, DownloadState.video_link, message.chat.id)
    bot.send_message(message.chat.id, '👀 Отправь мне ссылку на видео')


@bot.message_handler(state=DownloadState.video_link)
def bot_video_link(message: Message) -> None:
    if is_link_valid(message.text):
        video_url = message.text
        video_title = get_video_title(video_url)
        video_image = get_video_image(video_url)
        text = f'⏳ Начинаю скачивание {video_title}'
        bot.send_photo(message.chat.id, photo=video_image, caption=text)
        download_video(message.chat.id, message.from_user.id, video_title,
                       video_url)
        bot.delete_state(message.chat.id, message.from_user.id)
    else:
        bot.send_message(message.chat.id, '😔 Не могу использовать это видео. Возможные причины ошибки:\n'
                                          'Вы отправляете не ссылку на видео.\n'
                                          'Видео слишком длинное.')

