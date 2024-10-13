import requests
from config import settings


def send_tg_msg(message, chat_id):
    """ Отправка уведомления в Телеграм """
    params = {
        'text': message,
        'chat_id': chat_id,
    }
    requests.get(f'{settings.TG_URL}{settings.TG_BOT_TOKEN}/sendMessage', params=params)
