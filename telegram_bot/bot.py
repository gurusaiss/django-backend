import requests
from decouple import config

TOKEN = config('TELEGRAM_BOT_TOKEN')
URL = f'https://api.telegram.org/bot{TOKEN}/'

def get_updates():
    return requests.get(URL + 'getUpdates').json()

def handle_start(username):
    import django
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    django.setup()
    from api.models import TelegramUser
    TelegramUser.objects.get_or_create(username=username)

def poll():
    last_update_id = 0
    while True:
        updates = get_updates()
        for update in updates['result']:
            update_id = update['update_id']
            if update_id > last_update_id:
                last_update_id = update_id
                message = update['message']
                if message.get('text') == '/start':
                    username = message['from']['username']
                    handle_start(username)
