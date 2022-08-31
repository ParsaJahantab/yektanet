
import telebot
import requests
#from models import *
API_TOKEN = '5774491533:AAHhtnS7yn2GEqsXyvwzcpZe-T6lpFLxK5g'

bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    username = message.from_user.username
    chat_id = message.chat.id
    response = requests.get(f"http://127.0.0.1:8000/apt/users/telegram/{username}/{chat_id}")
    bot.reply_to(message, f"""
    this is your interview date : {response.json()}
    """)


@bot.message_handler()
def echo_message(message):
    bot.reply_to(message, message)


bot.infinity_polling()

