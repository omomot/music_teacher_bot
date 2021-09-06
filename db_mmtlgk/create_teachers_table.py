import mysql.connector
from mysql.connector import Error

def create_teachers(db):
    crsr = db.cursor()
    using = "USE mtb_db"
    query = """
    CREATE TABLE IF NOT EXISTS teachers(
        id INT AUTO_INCREMENT,
        psswrd VARCHAR(100),
        number_pup INT
    ) ENGINE = InnoDB
    """
    try:
        crsr.execute(using)
        crsr.execute(query)
        db.commit()
        print("Teachers table created succesfully")
    except Error as e:
        print(f"Error {e} occured")