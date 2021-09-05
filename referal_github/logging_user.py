import mysql.connector
from mysql.connector import Error

def log(db, telgr_id, password):
    using = "USE referal_db"
    query = f""" 
        SELECT psswrd FROM users WHERE tg_id = {telgr_id} 
    """
    crsr = db.cursor()
    crsr.execute(using)
    try:
        crsr.execute(query)
        fetched = crsr.fetchone()
        result = fetched[0]
        print(result)
        if result == password:
            return True
        else:
            return False
    except Error as e:
        print(f"The error '{e}' occured")