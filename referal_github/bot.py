from mysql.connector.errors import Error
import telebot
import config
import mysql.connector

import create_db
from create_table import create_users_table
from add_user import insert_user
from check_data import check_user
from logging_user import log
from get_balance import get_balance
from update_logging import update_log_status
from check_logging import check_log_status
from generations import generate_link
import update_balance_num_of_subs

from COMMANDS import cmds

bot = telebot.TeleBot(config.token)

global db
db = create_db.create_and_connect()
create_users_table(db)
db.close()



@bot.message_handler(commands = ['start'])
def send_welcome(message):
    print(message)
    bot.send_message(message.chat.id, "Hi")
    bot.send_message(message.chat.id, "Sign/Log in")
    bot.send_message(message.chat.id, "/help for more information")

@bot.message_handler(commands = ['help'])
def help_user(message):
    for cmd in cmds:
        bot.send_message(message.chat.id, f"{cmd} - {cmds[cmd]}")    
# ************************************************
@bot.message_handler(commands = ['Sign_in'])
def Signing_user(message):
    print(message.from_user.id)
    db = create_db.connect("localhost", "root", "Root_Root_12")
    if check_user(db, message.from_user.id) == 0:
        bot.send_message(message.chat.id, "Please create your own password and remember it")
        step = 'sign'
        bot.register_next_step_handler(message, lambda temp: get_from_user_password(step, temp))
    else:
        bot.send_message(message.chat.id, "You're already signed in! Please /Log_in")
    db.close()

def get_from_user_password(step, message):
    psswrd = message.text
    bot.send_message(message.chat.id, 'For security message with your password will be deleted from chat')
    bot.delete_message(message.chat.id, message.message_id)
    
    if (step == 'sign'):
        
        bot.send_message(message.chat.id, "Please always specify id of user, who invited you, if somebody did. If nodody did - print '-1'")
        bot.register_next_step_handler(message, lambda temp: get_from_user_id(psswrd, temp))
    
    elif step == 'log':
        db = create_db.connect("localhost", "root", "Root_Root_12")

        if log(db, message.from_user.id, psswrd) == True:
            bot.send_message(message.chat.id, 'Logging successful')
            update_log_status(db, message.from_user.id, 1)
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text = 'Check balance', callback_data = 'balance'))
            markup.add(telebot.types.InlineKeyboardButton(text = 'Generate unique inviting link', callback_data = 'link'))
            markup.add(telebot.types.InlineKeyboardButton(text = 'Leave system', callback_data = 'leave'))
            bot.send_message(message.chat.id, "What do you want to do?", reply_markup = markup)
            db.close()
        else:
            bot.send_message(message.chat.id, "Wrong password")
        
            
        db.close()
        
@bot.callback_query_handler(func = lambda call: True)
def query_handler(call):
    print(call)
    
    db = create_db.connect("localhost", "root", "Root_Root_12")
    if call.data == 'balance':
        if check_log_status(db, call.from_user.id) == 'logged':
            result = get_balance(db, call.from_user.id)
            bot.send_message(call.from_user.id, f"Your balance: ${result}")
        else:
            bot.send_message(call.from_user.id, "You are not loged in")
    elif call.data == 'link':
        if check_log_status(db, call.from_user.id) == 'logged':
            bot.send_message(call.from_user.id, "Here is ypur inviting link. Send it to your friends, and you wil get $10 on your balance")
            bot.send_message(call.from_user.id, generate_link(call.from_user.id))
        else:
            bot.send_message(call.from_user.id, "You are not loged in")
    elif call.data == 'leave':
        
        # leave_system
        if check_log_status(db, call.from_user.id) == 'logged':
            update_log_status(db, call.from_user.id, 0)
            bot.send_message(call.from_user.id, "Bye")
        else:
            bot.send_message(call.from_user.id, "You are not loged in")

    
    db.close()
            


def get_from_user_id(psswrd, message):
    text = message.text
    print(psswrd, text)
    db = create_db.connect("localhost", "root", "Root_Root_12")
    try:
        id = text
        print(f"id = {id}")
        insert_user(db, psswrd,  0, message.from_user.id, 0, text, 0)
        bot.send_message(message.chat.id, "Signing successful. /Log_in")
        update_balance_num_of_subs.update_bal(db, message.from_user.id)
        
        print(f"id = {id}")
        
        if id != '-1':
            # print(f"Kakogo huya& {id}")            
            update_balance_num_of_subs.update_bal(db, id)
            update_balance_num_of_subs.update_num(db, id)
        

    except Error as e:
        print(f"The error '{e}' occured")
    db.close()
# ************************************************

@bot.message_handler(commands = ['Log_in'])
def logging_user(message):
    db = create_db.connect("localhost", "root", "Root_Root_12")

    if check_user(db, message.from_user.id) == 0:
        bot.send_message(message.chat.id, 'You are not signed in the system. /Sign_in for signing in')
    else:
        if check_log_status(db, message.from_user.id) == 'not_logged':
            bot.send_message(message.chat.id, "Please verify your password")    
            step = 'log'
            bot.register_next_step_handler(message, lambda temp: get_from_user_password(step, temp))
        else:
            bot.send_message(message.chat.id, 'You are already loged in the system')
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text = 'Check balance', callback_data = 'balance'))
            markup.add(telebot.types.InlineKeyboardButton(text = 'Generate unique inviting link', callback_data = 'link'))
            markup.add(telebot.types.InlineKeyboardButton(text = 'Leave system', callback_data = 'leave'))
            bot.send_message(message.chat.id, "Choose what you want to do", reply_markup = markup)
    db.close()

@bot.callback_query_handler(func = lambda call: True)
def query_handler(call):
    print(call)
    db = create_db.connect("localhost", "root", "Root_Root_12")
    
    if call.data == 'balance':
        if check_log_status(db, call.from_user.id) == 'logged':
            result = get_balance(db, call.from_user.id)
            bot.send_message(call.from_user.id, f"Your balance: ${result}")
        else:
            bot.send_message(call.from_user.id, "You are not loged in")
    elif call.data == 'link':
        if check_log_status(db, call.from_user.id) == 'logged':
            bot.send_message(call.from_user.id, "Here is ypur inviting link. Send it to your friends, and you wil get $10 on your balance")
            bot.send_message(call.from_user.id, generate_link(call.from_user.id))
        else:
            bot.send_message(call.from_user.id, "You are not loged in")
    elif call.data == 'leave':
        
        # leave_system
        if check_log_status(db, call.from_user.id) == 'logged':
            update_log_status(db, call.from_user.id, 0)
            bot.send_message(call.from_user.id, "Bye")
        else:
            bot.send_message(call.from_user.id, "You are not loged in")
        
    

    
    db.close()

bot.polling()