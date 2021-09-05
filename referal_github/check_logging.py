import mysql.connector
from mysql.connector import Error

def check_log_status(db, telegram_id):
    using = "USE referal_db"
    query = f""" 
        SELECT IsLogged FROM users WHERE tg_id = {telegram_id} 
    """
    crsr = db.cursor()
    crsr.execute(using)
    try:
        crsr.execute(query)
        fetched = crsr.fetchone()
        result = fetched[0]
        print(result)
        if result == 1:
            return 'logged'
        else:
            return 'not_logged'
    except Error as e:
        print(f"The error '{e}' occured")
    