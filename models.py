import sqlite3 as sql
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite")


def add_new_user(name, telegram_id):
    con = sql.connect(db_path)
    cur = con.cursor()
    cur.execute("INSERT INTO main.users(name,telegram_id,balance ) "
                "VALUES(?, ?,0)", (name, telegram_id))
    con.commit()


def get_balance(telegram_id):
    con = sql.connect(db_path)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT balance FROM main.users where telegram_id = ?", [telegram_id])
    balance = cur.fetchone()[0]
    con.close()
    return balance


def get_tiсket(telegram_id):
    con = sql.connect(db_path)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT value FROM main.TICKETS where telegram_id = ?", [telegram_id])
    ticket = cur.fetchone()[0]
    con.close()
    return ticket


def add_ticket(value, telegram_id):
    con = sql.connect(db_path)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("INSERT INTO main.TICKETS(value,telegram_id) VALUES(?, ?)", (value, telegram_id))
    con.commit()


def add_balance(payment_amount, telegram_id):
    con = sql.connect(db_path)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("update USERS set balance = ? where telegram_id = ?", [payment_amount, telegram_id])
    con.commit()
