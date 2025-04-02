
import sqlite3
import os
from datetime import datetime

DB_PATH = "history.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS uploads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT,
            check_number TEXT,
            filename TEXT,
            method TEXT,
            status TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_upload(patient_name, check_number, filename, method, status):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO uploads (patient_name, check_number, filename, method, status, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (patient_name, check_number, filename, method, status, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM uploads ORDER BY timestamp DESC")
    rows = cur.fetchall()
    conn.close()
    return rows
