import mysql.connector
from mysql.connector import Error

def create_and_connect():
    def create_connection(host_name, user_name, user_password):
        db = None
        try:
            db = mysql.connector.connect(
                host = host_name,
                user = user_name,
                password = user_password
            )
            print("Connection successful")
        except Error as e:
            print(f"The error '{e}' ocured")
        
        return db

    db = create_connection("localhost", "root", "Root_Root_12")

    def create_database(db, query):
        crsr = db.cursor()
        try:
            crsr.execute(query)
            print("DB created successfully")
        except Error as e:
            print("The error '{e}' occured")

    create_db_query = "CREATE DATABASE IF NOT EXISTS referal_db"
    create_database(db, create_db_query)
    
    return db

def connect(host_name, user_name, user_password):
    db = None
    try:
        db = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password
        )
        print("Connection successful")
    except Error as e:
        print(f"The error '{e}' ocured")
        
    return db