from telebot import TeleBot, types
TOKEN = '5848062866:AAFjX1Q5AhPaNO8WjqkatNKn_DdBikZiUX4'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    lst = ['+', '-', '*', '/']
    bot.send_message(chat_id=msg.from_user.id, text=f'Введите арифметическую операцию \n{" ".join(lst)}')


@bot.message_handler()
def answer(msg: types.Message):
 
    text = msg.text
 
    if text == '+':
        bot.register_next_step_handler(msg, answer1)
        bot.send_message(chat_id=msg.from_user.id, text='Введите слагаемые')
    elif text == '-':
        bot.register_next_step_handler(msg, answer2)
        bot.send_message(chat_id=msg.from_user.id, text='Введите уменьшаемое и вычитаемое')
    elif text == '*':
        bot.register_next_step_handler(msg, answer3)
        bot.send_message(chat_id=msg.from_user.id, text='Введите множимое и множитель')
    elif text == '/':
        bot.register_next_step_handler(msg, answer4)
        bot.send_message(chat_id=msg.from_user.id, text='Введите делимое и делитель')
    
    else:
        bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text +
                                                        ', а должны были арифметическое действие')
 
 
def answer1(msg):
    a, b = map(float, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')
 
 
def answer2(msg):
    a, b = map(float,  msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {a - b}')

def answer3(msg):
    a, b = map(float,  msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат умножения {a * b}')

def answer4(msg):
    a, b = map(float,  msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат деления {a * b}')

 
 
bot.polling()







 
 
