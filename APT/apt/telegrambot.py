
import telebot
import requests

API_TOKEN = '5774491533:AAHhtnS7yn2GEqsXyvwzcpZe-T6lpFLxK5g'

bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    # username = message.from_user.username
    # response = requests.get(f"http://127.0.0.1:8000/apt/users/telegram/{username}")

    bot.reply_to(message, f"""
    this is your interview date :
    """)


@bot.message_handler()
def echo_message(message):
    bot.reply_to(message, message)


bot.infinity_polling()

