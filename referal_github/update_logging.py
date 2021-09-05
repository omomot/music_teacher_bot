import mysql.connector
from mysql.connector import Error

def update_log_status(db, telegram_id, status):
    using = "USE referal_db"
    query = f""" 
        UPDATE
            users
        SET
            IsLogged = {status}
        WHERE
            tg_id = {telegram_id}
    """
    crsr = db.cursor()
    crsr.execute(using)
    try:
        crsr.execute(query)
        db.commit()
        print("Updating successful successful")
    except Error as e:
        print(f"The error '{e}' occured")
    
    