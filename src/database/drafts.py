from database.client import close_db, connect_to_db, run_query


def save_current_draft(chat_id: str, message: str) -> None:
    conn = connect_to_db()
    run_query(conn, """
        INSERT INTO state (chat_id, draft, updated_at)
        VALUES (?, ?, CURRENT_TIMESTAMP)
        ON CONFLICT(chat_id) DO UPDATE SET
            draft      = excluded.draft,
            updated_at = CURRENT_TIMESTAMP
    """, (chat_id, message))
    close_db(conn)


def get_current_draft(chat_id: str) -> str | None:
    conn = connect_to_db()
    row = conn.execute(
        "SELECT draft FROM state WHERE chat_id = ?", (chat_id,)
    ).fetchone()
    close_db(conn)
    return row[0] if row else None


def approve_current_draft(chat_id: str) -> bool:
    conn = connect_to_db()
    row = conn.execute(
        "SELECT draft FROM state WHERE chat_id = ?", (chat_id,)
    ).fetchone()
    draft = row[0] if row else None
    if not draft:
        close_db(conn)
        return False
    conn.execute(
        "INSERT INTO drafts (chat_id, content) VALUES (?, ?)", (chat_id, draft)
    )
    conn.execute(
        "UPDATE state SET draft = NULL, updated_at = CURRENT_TIMESTAMP "
        "WHERE chat_id = ?", (chat_id,)
    )
    conn.commit()
    close_db(conn)
    return True


def get_approved_drafts(chat_id: str) -> list[str]:
    conn = connect_to_db()
    rows = conn.execute(
        "SELECT content FROM drafts WHERE chat_id = ? ORDER BY approved_at DESC",
        (chat_id,),
    ).fetchall()
    close_db(conn)
    return [r[0] for r in rows]
