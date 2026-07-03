from database.client import close_db, connect_to_db, run_query


def save_current_draft(chat_id: int, message: str) -> None:
    conn = connect_to_db()
    run_query(
        conn,
        """
        INSERT INTO state (chat_id, draft, updated_at)
        VALUES (?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(chat_id) DO UPDATE SET
            draft      = excluded.draft,
            updated_at = CURRENT_TIMESTAMP
    """,
        (chat_id, message),
    )
    close_db(conn)


def get_current_draft(chat_id: int) -> str:
    conn = connect_to_db()
    row = run_query(
        conn, "SELECT draft FROM state WHERE chat_id = ?", (chat_id,)
    ).fetchone()
    close_db(conn)
    return row[0] if row and row[0] else "No draft found!"


def approve_current_draft(chat_id: int) -> str:
    conn = connect_to_db()
    try:
        row = run_query(
            conn, "SELECT draft FROM state WHERE chat_id = ?", (chat_id,)
        ).fetchone()
        if not row or not row[0]:
            return "No draft found!"
        with conn:
            conn.execute(
                "INSERT INTO drafts (chat_id, content) VALUES (?, ?)", (chat_id, row[0])
            )
            conn.execute(
                "UPDATE state SET draft = NULL, updated_at = CURRENT_TIMESTAMP WHERE chat_id = ?",
                (chat_id,),
            )
    finally:
        close_db(conn)


def delete_memory(chat_id: int) -> str:
    conn = connect_to_db()
    try:
        run_query(
            conn,
            """
            DELETE FROM agent_messages WHERE session_id = ?
            """,
            (chat_id,),
        )

        run_query(
            conn,
            """
            DELETE FROM agent_sessions WHERE session_id = ?
            """,
            (chat_id,),
        )

        run_query(
            conn,
            """
            DELETE FROM state WHERE chat_id = ?
            """,
            (chat_id,),
        )
    finally:
        close_db(conn)
