import sqlite3

from config import SQLITE_DB_PATH


def connect_to_db() -> sqlite3.Connection:
    SQLITE_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(SQLITE_DB_PATH)


def run_query(conn: sqlite3.Connection, query: str, params=None) -> sqlite3.Cursor:
    cursor = conn.execute(query, params) if params is not None else conn.execute(query)
    conn.commit()
    return cursor


def close_db(conn: sqlite3.Connection) -> None:
    conn.close()
