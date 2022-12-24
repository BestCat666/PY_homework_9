import pandas
import openpyxl
from telebot import TeleBot, types
import os
os.chdir(os.path.dirname(__file__))
 
TOKEN = '5644346942:AAHdonF5jp5F55D0KWf1ZBdOOfsyTwIay8s'
 
bot = TeleBot(TOKEN)

# @bot.message_handler(commands=['start', 'help'])
# def answer(msg: types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text='Введите номер операции: 1 - добавление записи, 2 - вывод записи на экран, 3 - импорт, 4 - экспорт, 5 - выход из программы')


# @bot.message_handler()
# def answer(msg: types.Message):
#     text = msg.text
#     if text == '3':
#         bot.send_message(chat_id=msg.from_user.id, text='Добавьте документ для импортирования')
#         bot.register_next_step_handler(msg, answer3)



