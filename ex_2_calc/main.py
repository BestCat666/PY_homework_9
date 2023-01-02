from telebot import TeleBot, types
#import logger1
import os
import datetime
file = 'logger.txt'
now = str(datetime.datetime.now())
os.chdir(os.path.dirname(__file__))

TOKEN = ''
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def answer1(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Введите номер операции: 1 - работа с простыми числами, 2 - работа с комплексными числами')

@bot.message_handler()   
def answer2(msg: types.Message):
    text = msg.text
    lst = ['+', '-', '*', '/']     
    if text == '1':  
        bot.register_next_step_handler(msg, answer3)               
        bot.send_message(chat_id=msg.from_user.id, text=f'Введите арифметическую операцию \n{" ".join(lst)}')
    elif text == '2': 
        bot.register_next_step_handler(msg, answer8)               
        bot.send_message(chat_id=msg.from_user.id, text=f'Введите арифметическую операцию \n{" ".join(lst)}')
    else:
        bot.register_next_step_handler(msg, answer1) 
        bot.send_message(chat_id=msg.from_user.id, text=f'!Ошибка. Пожалуйста, введите номер операции: 1 - работа с простыми числами, 2 - работа с комплексными числами')

@bot.message_handler()
def answer3(msg: types.Message):
    text = msg.text
    if text == '+':
        bot.register_next_step_handler(msg, answer4)
        bot.send_message(chat_id=msg.from_user.id, text='Введите слагаемые через пробел')
    elif text == '-':
        bot.register_next_step_handler(msg, answer5)
        bot.send_message(chat_id=msg.from_user.id, text='Введите уменьшаемое и вычитаемое через пробел')
    elif text == '*':
        bot.register_next_step_handler(msg, answer6)
        bot.send_message(chat_id=msg.from_user.id, text='Введите множимое и множитель через пробел')
    elif text == '/':
        bot.register_next_step_handler(msg, answer7)
        bot.send_message(chat_id=msg.from_user.id, text='Введите делимое и делитель через пробел')
    else:
        bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text +
                                                        ', а должны были арифметическое действие')

def answer4(msg):
    a, b = map(float, msg.text.split())
    # if type(a) == int or float and type(b) == int or float:
    # if a.isdigit() and b.isdigit():
    res = a + b
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {res}')
    data = f"Пользователь ввёл слогаемые: {msg.text}, результат: {res}, время: {now}"
    with open('logger.txt', 'a+', encoding='utf-8') as file:
        file.write(data + '\n')
    # else:
    #     bot.send_message(chat_id=msg.from_user.id, text='Введите, пожалуйста, числа!')

def answer5(msg):
    a, b = map(float,  msg.text.split())
    res = a - b
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {res}')
    data = f"Пользователь ввёл уменьшаемое и вычитаемое: {msg.text}, результат: {res}, время: {now}"
    with open('logger.txt', 'a+', encoding='utf-8') as file:
        file.write(data + '\n')

def answer6(msg):
    a, b = map(float,  msg.text.split())
    res = a * b
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат умножения {res}')
    data = f"Пользователь ввёл множимое и множитель: {msg.text}, результат: {res}, время: {now}"
    with open('logger.txt', 'a+', encoding='utf-8') as file:
        file.write(data + '\n')

def answer7(msg):
    a, b = map(float,  msg.text.split())
    res = a / b
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат деления {a / b}')
    data = f"Пользователь ввёл делимое и делитель: {msg.text}, результат: {res}, время: {now}"
    with open('logger.txt', 'a+', encoding='utf-8') as file:
        file.write(data + '\n')

@bot.message_handler() 
def answer8(msg: types.Message):
    text = msg.text
    if text == '+':
        bot.register_next_step_handler(msg, answer9)
        bot.send_message(chat_id=msg.from_user.id, text='Введите четыре числа через пробел для составления комплексных чисел: ')
    if text == '-':
        bot.register_next_step_handler(msg, answer10)
        bot.send_message(chat_id=msg.from_user.id, text='Введите четыре числа через пробел для составления комплексных чисел: ')
    if text == '/':
        bot.register_next_step_handler(msg, answer11)
        bot.send_message(chat_id=msg.from_user.id, text='Введите четыре числа через пробел для составления комплексных чисел: ')
    if text == '*':
        bot.register_next_step_handler(msg, answer12)
        bot.send_message(chat_id=msg.from_user.id, text='Введите четыре числа через пробел для составления комплексных чисел: ')

def answer9(msg):
    a, b, c, d = map(int, msg.text.split())
    g = complex(a,b)
    k = complex(c,d)
    res = g + k
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {res}')
    data = f"Пользователь ввёл: {msg.text}, результат: {res}, время: {now}"
    with open('logger.txt', 'a+', encoding='utf-8') as file:
        file.write(data + '\n')

def answer10(msg):
    a, b, c, d = map(int, msg.text.split())
    g = complex(a,b)
    k = complex(c,d)
    res = g - k
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {res}')
    data = f"Пользователь ввёл: {msg.text}, результат: {res}, время: {now}"
    with open('logger.txt', 'a+', encoding='utf-8') as file:
        file.write(data + '\n')

def answer11(msg):
    a, b, c, d = map(int, msg.text.split())
    g = complex(a,b)
    k = complex(c,d)
    res = g / k
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат деления {res}')
    data = f"Пользователь ввёл: {msg.text}, результат: {res}, время: {now}"
    with open('logger.txt', 'a+', encoding='utf-8') as file:
        file.write(data + '\n')

def answer12(msg):
    a, b, c, d = map(int, msg.text.split())
    g = complex(a,b)
    k = complex(c,d)
    res = g * k
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат умножения {res}')
    data = f"Пользователь ввёл: {msg.text}, результат: {res}, время: {now}"
    with open('logger.txt', 'a+', encoding='utf-8') as file:
        file.write(data + '\n')

bot.polling()




 








 
 
