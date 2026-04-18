import requests
from core.logger import logger

def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot8735658793:AAH0ernTliFXty3bBxQoSA6ABkDKh_06T7E/sendMessage"

    payload = {
        "chat_id":841046255,
        "text":message
    }

    response = requests.post(url, json=payload)
    if response.status_code != 200:
        logger.error(f"{response.text}")