import mysql.connector
from mysql.connector import Error

def create_pupils(db):
    crsr = db.cursor()
    using = "USE mtb_db"
    query = """
    CREATE TABLE IF NOT EXISTS pupils(
        id INT AUTO_INCREMENT,
        psswrd VARCHAR(100),
        teacher_id INT,
        level INT
    ) ENGINE = InnoDB
    """
    try:
        crsr.execute(using)
        crsr.execute(query)
        db.commit()
        print("Pupils table created succesfully")
    except Error as e:
        print(f"Error {e} occured")