import sqlite3

def create_database():
    database = sqlite3.connect('database.db')
    database.commit()
    return database
def connect_database():
    database = sqlite3.connect('database.db')
    return database
def create_table():
    database = sqlite3.connect('database.db')
    database_cursor = database.cursor()
    database_cursor.execute(
        "CREATE TABLE IF NOT EXISTS users(name text not null, email text not null unique, password text)")
def insert_user(name, email, password):
    database = sqlite3.connect('database.db')
    database_cursor = database.cursor()
    database_cursor.execute("INSERT INTO users(name, email, password) VALUES (?, ?, ?)", (name, email, password))
    database.commit()
    database.close()
def search_user(email):
    database = sqlite3.connect('database.db')
    database_cursor = database.cursor()
    database_cursor.execute(
        "SELECT name, password FROM users WHERE email=?", (email,))
    result = database_cursor.fetchone()
    database.close()
    if result:
        return result 
    else:
        None