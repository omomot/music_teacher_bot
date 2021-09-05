import mysql.connector
from mysql.connector.errors import Error

def create_and_connect():
    def create_connection(host_name, user_name, password):
        db = None
        try:
            db = mysql.connector.connect(
                host = host_name,
                user = user_name,
                password = password
            )
            print("Connection succesful")
        except Error as e:
            print(f"Error {e} occured")

        return db
    
    db = create_connection("localhost", "root", "Root_Root_12")

    def create_database(db, query):
        crsr = db.cursor()
        try:
            crsr.execute(query)
            print("DB created succesfully")
        except Error as e:
            print(f"Error {e} occured")

    create_db_query = "CREATE DATABASE IF NOT EXISTS mtb_db"
    create_database(db, create_db_query)

    return db

def connect(host_name, user_name, password):
    db = None
    try:
        db = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = password
        )
        print("Connection succesful")
    except Error as e:
        print(f"Error {e} occured")

    return db
    
