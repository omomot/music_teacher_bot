import telebot
# import add_user!!!


def signing_user(db, bot, message):
    
    psswrd = bot.send_message(message.chat.id, "Будь ласка введіть пароль. Пароль буде видалено із чату задля безопасності, тому запам'ятайте його")
    
    def get_password(psswrd):
        return psswrd.text
    
    password = get_password(psswrd)
# ********************************************
    tchr = bot.send_message(message.chat.id, "Пропоную Вам ознайомитися із списком вчителів, які працюють зі мною. Вони зможуть підібрати найбільш досконалу індивідуальну программу навчання. Скопіюйте та введіть id вчителя, якого Ви вважаєте найбільш підходящим для Вас. Якщо ви не хочете, щоб Ваші досягнення контролював вчитель - введіть - \'-1\'")

    def get_teacher(tchr):
        return tchr.text

    teacher = get_teacher(tchr)
# ********************************************
    lvl = bot.send_message(message.chat.id, "Будь ласка, оцініть Ваш рівенб знань. 0 - Низький, 1 - Нижче середнього, 2 - Середній, 3 - Вище середнього, 4 - Достатній, 5 - Високий")

    def get_level(lvl):
        return lvl.text

    level = get_level(lvl)
# ********************************************
    add_user(db, password, teacher, level)

