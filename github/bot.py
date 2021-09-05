import telebot
import config
from COMMANDS import cmds
from activities import acts
from info import description
# *****************************************MYSQL**************************************
import mysql.connector
from mysql.connector.errors import Error
# **************************************************************************************
bot = telebot.TeleBot(config.token)

# **************************************************************************************
@bot.message_handler(commands = ['start'])
def send_welcome(message):
    print(message)
    bot.send_message(message.chat.id, "Доброго дня! Я бот-вчитель музичної грамоти. Я допоможу Вам розібратися у таких предметах, як сольфеджіо та музична література. /help - для більшого")
    # keyboard = telebot.types.InlineKeyboardMarkup(row_width = 2)
    # keyboard.add(telebot.types.InlineKeyboardButton(text = "Сольфеджіо", callback_data = 'sol'))
    # keyboard.add(telebot.types.InlineKeyboardButton(text = "Музична література", callback_data = 'mus_lit'))
    # keyboard.add(telebot.types.InlineKeyboardButton(text = "Виклик!", callback_data = 'challange'))
    # bot.send_message(message.chat.id, "Чим бажаєте зайнятися сьогодні?", reply_markup = keyboard)

# @bot.callback_query_handler(func  = lambda call: call.data == 'sol' or call.data == 'mus_lit' or call.data == 'challange')
# def choose_activity(call):
#     pass

@bot.message_handler(commands = ['help'])
def help_user(message):
    str = ''
    bot.send_message(message.chat.id, "Доступні команди:")
    for cmd in cmds:
        str += f"{cmd} - {cmds[cmd]}"
        str += "\n"
    bot.send_message(message.chat.id, str)

@bot.message_handler(commands = ['activity'])
def choose_activity(message):
    str = ''
    bot.send_message(message.chat.id, "Доступні дії:")
    for act in acts:
        str += f"{act} - {acts[act]}"
        str += "\n"
    bot.send_message(message.chat.id, str)

@bot.message_handler(commands = ['about'])
def tell_about(message):
    bot.send_message(message.chat.id, description)
# **************************************************************************************





    # bot.send_message(message.chat.id, "Будь ласка, оцініть Ваш рівень музичних знань")
    # markup = telebot.types.InlineKeyboardMarkup()
    # markup.add(telebot.types.InlineKeyboardButton(text = 'Низький', callback_data = 'low'))
    # markup.add(telebot.types.InlineKeyboardButton(text = 'Середній', callback_data = 'average'))
    # markup.add(telebot.types.InlineKeyboardButton(text = 'Високий', callback_data = 'high'))
    # bot.send_message(message.chat.id, """Сольфеджіо — дисципліна, що розвиває уміння чути й слухати музику, а також інтонаційно та ритмічно точно, виразно і свідомо створювати музичний текст. 
    # Сольфеджіо спрямоване на виховання та розвиток музичного слуху (в тому числі так званого внутрішнього слуху) та музичної пам'яті. 
    # Включає сольфеджування (спів по нотах з вимовлянням назви кожного звуку), слуховий аналіз музики та її запис (музичний диктант).
    # Сприяє зв'язку теорії музики з музичною практикою. Оцініть Ваш рівень знань (низький - не розумію взагалі (початківець); середній - розумію, проте погано, маю музичний досвід; високий - дуже добре розумію, хочу вдосконалити свої знання)""", reply_markup = markup)

# @bot.callback_query_handler(func=lambda call: True)
# def query_handler(call):
#     bot.answer_callback_query(callback_query_id = call.id, text = "Дякую за відповідь")
#     answer = ''
#     if call.data == 'low':
#         answer = 'Низький. Зрозумів. Починаю пошук програми для Вас...'
#     elif call.data == 'average':
#         answer = 'Середній. Зрозумів. Починаю пошук програми для Вас...'    
#     elif call.data == 'high':
#         answer = 'Високий. Зрозумів. Починаю пошук програми для Вас...'    
#     bot.send_message(call.message.chat.id, answer)
#     bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

bot.polling()