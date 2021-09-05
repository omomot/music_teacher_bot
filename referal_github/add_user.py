import mysql.connector
from mysql.connector import Error

def insert_user(db, psswrd, bal, telegram_id, num_sub, from_user, logged):
    print(f"HAHA {psswrd}, {bal}, {telegram_id}, {num_sub}, {from_user}")
    using = "USE referal_db"
    query = """ 
        INSERT INTO users(psswrd, balance, tg_id, num_subordinates, from_user_id, IsLogged) VALUES (%s, %s, %s, %s, %s, %s)
    """
    args = (psswrd, bal, telegram_id, num_sub, from_user, logged)
    crsr = db.cursor()
    crsr.execute(using)
    try:
        crsr.execute(query, args)
        db.commit()
        print("Insertion successful")
    except Error as e:
        print(f"The error '{e}' occured")
    
    