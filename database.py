import sqlite3


conn = sqlite3.connect("sqlite.db")
cur = conn.cursor()

def create_user_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        battletag TEXT
    );
    """)
    conn.commit()


def add_user(user_id, name):
    cur.execute(
        "INSERT INTO Users (id, name) VALUES (?, ?)",
        (user_id, name))
    conn.commit()


def get_user_name(user_id):
    cur.execute(
        "SELECT name FROM Users WHERE id = ?",
        (user_id,))
    return cur.fetchone()


def get_battletag(user_id):
    cur.execute(
        "SELECT battletag FROM Users WHERE id = ?",
        (user_id,))
    return cur.fetchone()

def set_battletag(user_id, battletag):
    cur.execute(
        "UPDATE Users SET battletag = ? WHERE id = ?",
        (battletag, user_id))
    conn.commit()

def close():
    conn.close()