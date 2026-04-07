import sqlite3
from datetime import datetime
from flask import request

DB_PATH = "visitas.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def inicializar_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            ruta TEXT,
            origen TEXT,
            fecha TEXT
        )
    ''')

    # 🔥 índice para que las consultas vayan rápidas
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_origen_fecha 
        ON visitas (origen, fecha)
    ''')

    conn.commit()
    conn.close()


def registrar_visita(origen="directo"):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO visitas (ip, ruta, origen, fecha)
        VALUES (?, ?, ?, ?)
    ''', (
        request.remote_addr,
        request.path,
        origen,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()