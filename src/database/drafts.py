from database.client import close_db, connect_to_db, run_query


def save_current_draft(chat_id: int, message: str) -> None:
    conn = connect_to_db()
    run_query(conn, """
        INSERT INTO state (chat_id, draft, updated_at)
        VALUES (?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(chat_id) DO UPDATE SET
            draft      = excluded.draft,
            updated_at = CURRENT_TIMESTAMP
    """, (chat_id, message))
    close_db(conn)


def get_current_draft(chat_id: int) -> str | None:
    conn = connect_to_db()
    row = run_query(
        conn, "SELECT draft FROM state WHERE chat_id = ?", (chat_id,)
    ).fetchone()
    close_db(conn)
    return row[0] if row else None


def approve_current_draft(chat_id: int) -> bool:
    conn = connect_to_db()
    try:
        row = run_query(
            conn, "SELECT draft FROM state WHERE chat_id = ?", (chat_id,)
        ).fetchone()
        if not row or not row[0]:
            return False
        with conn:
            conn.execute(
                "INSERT INTO drafts (chat_id, content) VALUES (?, ?)", (chat_id, row[0])
            )
            conn.execute(
                "UPDATE state SET draft = NULL, updated_at = CURRENT_TIMESTAMP WHERE chat_id = ?",
                (chat_id,),
            )
        return True
    finally:
        close_db(conn)


def get_approved_drafts(chat_id: int) -> list[str]:
    conn = connect_to_db()
    rows = run_query(
        conn,
        "SELECT content FROM drafts WHERE chat_id = ? ORDER BY approved_at DESC",
        (chat_id,),
    ).fetchall()
    close_db(conn)
    return [r[0] for r in rows]
