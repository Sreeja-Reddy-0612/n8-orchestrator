import sqlite3
import json

DB_FILE = "executions.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS executions (
            execution_id TEXT PRIMARY KEY,
            status TEXT,
            result TEXT,
            trace TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_execution(execution):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO executions 
        (execution_id, status, result, trace)
        VALUES (?, ?, ?, ?)
    """, (
        execution["execution_id"],
        execution["status"],
        json.dumps(execution["result"]),
        json.dumps(execution["trace"])
    ))

    conn.commit()
    conn.close()


def list_executions():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT execution_id, status 
        FROM executions
        ORDER BY rowid DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return [
        {"execution_id": row[0], "status": row[1]}
        for row in rows
    ]


def get_execution(execution_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT execution_id, status, result, trace
        FROM executions
        WHERE execution_id = ?
    """, (execution_id,))

    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    return {
        "execution_id": row[0],
        "status": row[1],
        "result": json.loads(row[2]),
        "trace": json.loads(row[3])
    }