import sqlite3

DB_NAME = "bfaf.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor() 

    # ==========================
    # Tabela de pacientes
    # ==========================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        medication TEXT,
        disease TEXT,
        professional_name TEXT
    )
    """)

    # ==========================
    # Tabela de respostas
    # ==========================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
    conn.close()


# =====================================================
# PACIENTES
# =====================================================

def save_patient(patient_name, medication, disease, professional_name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO patients (
            patient_name, medication, disease, professional_name
        )
        VALUES (?, ?, ?, ?)
    """, (patient_name, medication, disease, professional_name))

    conn.commit()
    pid = cur.lastrowid
    conn.close()
    return pid


def get_all_patients():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM patients ORDER BY id")
    rows = cur.fetchall()

    conn.close()
    return [dict(r) for r in rows]


# =====================================================
# RESPOSTAS
# =====================================================

def save_response(
    patient_id,
    question_id,
    alternativa,
    valor,
    open_text,
    judgement,
    is_barreira,
    is_facilitador,
    classificacao_texto
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO responses (
            patient_id,
            question_id,
            alternativa,
            valor,
            open_text,
            judgement,
            is_barreira,
            is_facilitador,
            classificacao_texto
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        patient_id,
        question_id,
        alternativa,
        valor,
        open_text,
        judgement,
        is_barreira,
        is_facilitador,
        classificacao_texto
    ))

    conn.commit()
    conn.close()


def get_responses_by_patient(patient_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM responses
        WHERE patient_id = ?
        ORDER BY question_id
    """, (patient_id,))

    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_all_responses():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM responses
        ORDER BY patient_id, question_id
    """)
    rows = cur.fetchall()

    conn.close()
    return [dict(r) for r in rows]


# =====================================================
# ESTATÍSTICAS
# =====================================================

def calculate_score_and_counts(patient_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            SUM(valor) AS total_score,
            SUM(is_barreira) AS total_barreiras,
            SUM(is_facilitador) AS total_facilitadores
        FROM responses
        WHERE patient_id = ?
    """, (patient_id,))

    row = cur.fetchone()
    conn.close()

    return {
        "total_score": row["total_score"] or 0,
        "total_barreiras": row["total_barreiras"] or 0,
        "total_facilitadores": row["total_facilitadores"] or 0
    }
