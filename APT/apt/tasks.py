from celery import shared_task
from .models import *
import telebot

API_TOKEN = '5774491533:AAHhtnS7yn2GEqsXyvwzcpZe-T6lpFLxK5g'

bot = telebot.TeleBot(API_TOKEN)

@shared_task
def send_timed_massage(chat_id,name,date):
    bot.send_message(chat_id=chat_id,text=f"""hello:{name} your interview is in an hour""")

