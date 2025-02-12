import sys

import requests
import logging
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
from telegram import BotCommand


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


CHAT_GPTI_API_URL = "https://chatgpt-42.p.rapidapi.com/o3mini"
HEADERS = {
    "x-rapidapi-key": "4893157a12mshe49c07deb8f4483p1757dejsnea57e7ec3428",
    "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
    "Content-Type": "application/json"
}


def get_chat_gpt_response(messages):
    payload = {
        "messages": [
            {
                "role": "user",
                "content": messages
            }
        ],
        "web_access": False
    }

    try:
        response = requests.post(CHAT_GPTI_API_URL, json=payload, headers=HEADERS)
        response.raise_for_status()


        data = response.json()


        print("API javobi:", data)


        if 'result' in data:
            return data['result']
        else:
            return "API javobida xatolik: 'result' topilmadi."
    except requests.exceptions.RequestException as e:
        logging.error(f"API so'rovida xatolik: {e}")
        return "Xatolik yuz berdi, iltimos keyinroq urinib ko'ring."
    except Exception as e:
        logging.error(f"Umumiy xatolik: {e}")
        return "Xatolik yuz berdi, iltimos keyinroq urinib ko'ring."


def start_func(update, context):
    commands=[BotCommand(command='start',description="botga start berish"),
    BotCommand(command='info',description="bot dasturchisi Xayrullayev Ma'murjon juda yaxshi dasturchi")]
    context.bot.set_my_commands(commands=commands)

    update.message.reply_text(text="Salom! Men Ma'mur AI botman. Sizga qanday yordam bera olaman?")


def handle_message(update, context):
    user_message = update.message.text
    chatgpt_response = get_chat_gpt_response(user_message)
    update.message.reply_text(chatgpt_response)


def main():

    TOKEN = "7668542203:AAGfxYaFe1B2ucFnBFS4x127cYNgiQLgdws"
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher


    dispatcher.add_handler(CommandHandler("start", start_func))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO,
                        handlers=[
                            logging.FileHandler("bot.log"),
                            logging.StreamHandler(sys.stdout)
                        ])
    main()