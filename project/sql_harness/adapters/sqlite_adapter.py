from __future__ import annotations
from pathlib import Path
import sqlite3


class SQLiteReadOnlyAdapter:
    """Starter adapter used by the through-project before MCP integration.

    Safety here is defense-in-depth, not the final verifier assignment.
    """

    def __init__(self, db_path: str | Path):
        self.db_path = Path(db_path)

    def get_schema(self, request: str = "") -> dict:
        with sqlite3.connect(self.db_path) as con:
            rows = con.execute("PRAGMA table_info(sales)").fetchall()
        return {
            "tables": {
                "sales": [
                    {"name": r[1], "type": r[2]} for r in rows
                ]
            }
        }

    def execute_readonly(self, sql: str) -> list[dict]:
        q = sql.strip()
        head = q.lower().lstrip("(")
        if not (head.startswith("select") or head.startswith("with")):
            raise PermissionError("Only SELECT/CTE queries are allowed")
        uri = f"file:{self.db_path}?mode=ro"
        con = sqlite3.connect(uri, uri=True)
        con.row_factory = sqlite3.Row
        try:
            return [dict(r) for r in con.execute(q).fetchall()]
        finally:
            con.close()
