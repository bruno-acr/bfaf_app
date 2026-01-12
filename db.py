import os
import sqlite3
import psycopg2
import psycopg2.extras

# O Render fornece a URL do banco na variável DATABASE_URL
DATABASE_URL = os.environ.get('DATABASE_URL')

def get_connection():
    # Se houver uma URL de banco (estamos no Render/Nuvem)
    if DATABASE_URL:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        # Configura para retornar dicionários, igual ao sqlite3.Row
        conn.cursor_factory = psycopg2.extras.DictCursor
        return conn
    
    # Se não houver URL (estamos rodando localmente no VS Code)
    else:
        conn = sqlite3.connect("bfaf.db")
        conn.row_factory = sqlite3.Row
        return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor() 

    # SQL compatível com SQLite e PostgreSQL
    cur.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id SERIAL PRIMARY KEY,
        patient_name TEXT,
        medication TEXT,
        disease TEXT,
        professional_name TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS responses (
        id SERIAL PRIMARY KEY,
        patient_id INTEGER,
        question_id INTEGER,
        alternativa TEXT,
        valor INTEGER,
        open_text TEXT,
        judgement TEXT,
        is_barreira INTEGER,
        is_facilitador INTEGER,
        classificacao_texto TEXT
    )
    """)

    conn.commit()
    cur.close()
    conn.close()

# O restante das suas funções (save_patient, save_response, etc) 
# continuam iguais, pois o código acima já resolve a conexão!
# Apenas certifique-se de usar cur.close() antes de conn.close() 
# em todas as funções para ser mais seguro.