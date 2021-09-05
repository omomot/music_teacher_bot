import mysql.connector
from mysql.connector import Error

def create_users_table(db):
    crsr = db.cursor()
    using = "USE referal_db"
    query = """
    CREATE TABLE IF NOT EXISTS users(
        id INT AUTO_INCREMENT,
        psswrd VARCHAR(100),
        balance INT,
        tg_id INT,
        num_subordinates INT,
        from_user_id INT,
        IsLogged INT,
        PRIMARY KEY (id)
    ) ENGINE = InnoDB
    """
    try:
        crsr.execute(using)
        crsr.execute(query)
        db.commit()
        print("Users table created successfully")
    except Error as e:
        print(f"The error '{e}' occured")
    
    
    