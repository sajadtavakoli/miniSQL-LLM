import re
import sqlite3
from typing import Optional, Tuple

def normalize_sql(sql: str) -> str:
    sql = sql.strip().rstrip(";")
    sql = re.sub(r"\s+", " ", sql)
    return sql.lower()

def exact_match(prediction: str, reference: str) -> bool:
    return normalize_sql(prediction) == normalize_sql(reference)

def is_valid_sql(sql: str, database_path: Optional[str] = None) -> Tuple[bool, str]:
    db = database_path or ":memory:"
    try:
        conn = sqlite3.connect(db)
        conn.execute(f"EXPLAIN QUERY PLAN {sql}")
        conn.close()
        return True, ""
    except Exception as exc:
        return False, str(exc)

def execute_sql(sql: str, database_path: str):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows
