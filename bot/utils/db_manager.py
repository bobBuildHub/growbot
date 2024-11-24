# utils/db_manager.py
import os
from tinydb import TinyDB
import psycopg2

db_type = os.getenv("DB_TYPE", "tinydb")

if db_type == "tinydb":
    db = TinyDB("database.json")

def insert_tinydb(data):
    db.insert(data)

def insert_postgresql(data):
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO users (id, name) VALUES (%s, %s)", (data["id"], data["name"]))
    conn.commit()
    conn.close()

def insert_data(data):
    if db_type == "tinydb":
        insert_tinydb(data)
    elif db_type == "postgresql":
        insert_postgresql(data)
