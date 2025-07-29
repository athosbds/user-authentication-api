import sqlite3


def create_database():
    database = sqlite3.connect('database.db')
    database.commit()
    return database


def create_table():
    database = sqlite3.connect('database.db')
    database_cursor = database.cursor()
    database_cursor.execute(
        "CREATE TABLE IF NOT EXISTS users(name text not null, email text not null unique, password text)")


def search_user(email):
    database = sqlite3.connect('database.db')
    database_cursor = database.cursor()
    database_cursor.execute(
        "SELECT password FROM users WHERE email=?", (email,))
    result = database_cursor.fetchone()
    database.close()
    if result:
        return result[0]
    else:
        None