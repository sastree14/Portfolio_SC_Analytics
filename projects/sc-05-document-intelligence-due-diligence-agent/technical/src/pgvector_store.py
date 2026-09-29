from __future__ import annotations
import psycopg

def nearest_chunks(conn: psycopg.Connection, embedding: list[float], limit: int = 5):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT chunk_id, document_id, content,
                   1 - (embedding <=> %s::vector) AS cosine_similarity
            FROM document_chunks
            ORDER BY embedding <=> %s::vector
            LIMIT %s
            """,
            (embedding, embedding, limit),
        )
        return cur.fetchall()
