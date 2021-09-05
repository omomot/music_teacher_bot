import mysql.connector
from mysql.connector import Error

def check_user(db, telgr_id):
    using = "USE referal_db"
    query = f""" 
        SELECT id FROM users WHERE tg_id = {telgr_id} 
    """
    crsr = db.cursor()
    crsr.execute(using)
    try:
        crsr.execute(query)
        result = crsr.fetchone()
        
        # print(result, "SIGNED")
        if result == None:
            return 0
        else:
            return 1
    except Error as e:
        print(f"The error '{e}' occured")