import mysql.connector
from mysql.connector import Error
from get_balance import get_balance
from get_number_of_subs import get_num

def update_bal(db, telegram_id):
    using = "USE referal_db"
    bal = get_balance(db, telegram_id)
    bal += 10
    update_bal_query = f""" 
        UPDATE
            users
        SET
            balance = {bal}
        WHERE
            tg_id = {telegram_id}
    """
    crsr = db.cursor()
    crsr.execute(using)
    try:
        crsr.execute(update_bal_query)
        db.commit()
        print("Updating successful successful")
    except Error as e:
        print(f"The error '{e}' occured")

def update_num(db, telegram_id):
    using = "USE referal_db"
    num = get_num(db, telegram_id)
    num += 1
    update_num_query = f""" 
        UPDATE
            users
        SET
            num_subordinates = {num}
        WHERE
            tg_id = {telegram_id}
    """
    crsr = db.cursor()
    crsr.execute(using)
    try:
        crsr.execute(update_num_query)
        db.commit()
        print("Updating successful successful")
    except Error as e:
        print(f"The error '{e}' occured")
    

    
    