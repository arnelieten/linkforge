from database.client import close_db, connect_to_db, run_query


def init_tables() -> None:
    conn = connect_to_db()
    run_query(conn, """
        CREATE TABLE IF NOT EXISTS state (
            chat_id    TEXT PRIMARY KEY,
            draft      TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    run_query(conn, """
        CREATE TABLE IF NOT EXISTS drafts (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id     TEXT NOT NULL,
            content     TEXT NOT NULL,
            approved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    close_db(conn)
