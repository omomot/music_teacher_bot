import mysql.connector
from mysql.connector import Error

def get_num(db, telgr_id):
    using = "USE referal_db"
    print(f"HAHAAHAH {telgr_id}")
    query = f""" 
        SELECT num_subordinates FROM users WHERE tg_id = {telgr_id} 
    """
    crsr = db.cursor()
    crsr.execute(using)
    try:
        crsr.execute(query)
        fetched = crsr.fetchone()
        result = fetched[0]
        print(result)
        return result
    except Error as e:
        print(f"The error '{e}' occured")