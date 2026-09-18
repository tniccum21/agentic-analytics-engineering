from __future__ import annotations

from pathlib import Path
import re
import sqlite3
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "project" / "data" / "northstar.db"

_LEADING_COMMENT = re.compile(r"^(?:\s|--[^\n]*(?:\n|$)|/\*.*?\*/)*", re.DOTALL)


class NorthstarService:
    """Read-only data service behind the course MCP server.

    The MCP layer is intentionally thin. Safety is enforced here as well as
    upstream in the SQL harness so Module 4 can demonstrate defense in depth.
    """

    def __init__(self, db_path: str | Path = DEFAULT_DB, max_rows: int = 200):
        self.db_path = Path(db_path)
        self.max_rows = max_rows

    def _connect(self) -> sqlite3.Connection:
        uri = f"file:{self.db_path}?mode=ro"
        con = sqlite3.connect(uri, uri=True)
        con.row_factory = sqlite3.Row
        con.execute("PRAGMA query_only = ON")
        return con

    @staticmethod
    def _first_keyword(sql: str) -> str:
        stripped = _LEADING_COMMENT.sub("", sql, count=1).lstrip()
        if not stripped:
            return ""
        return stripped.split(None, 1)[0].lower().rstrip(";")

    def _table_names(self) -> list[str]:
        with self._connect() as con:
            rows = con.execute(
                "SELECT name FROM sqlite_master "
                "WHERE type='table' AND name NOT LIKE 'sqlite_%' "
                "ORDER BY name"
            ).fetchall()
        return [str(row["name"]) for row in rows]

    def get_schema(self) -> dict[str, Any]:
        return {
            "database": "northstar-retail",
            "tables": {
                table: self.get_table_info(table)["columns"]
                for table in self._table_names()
            },
        }

    def get_table_info(self, table: str) -> dict[str, Any]:
        tables = self._table_names()
        if table not in tables:
            raise ValueError(f"Unknown Northstar table: {table}")
        quoted = table.replace('"', '""')
        with self._connect() as con:
            rows = con.execute(f'PRAGMA table_info("{quoted}")').fetchall()
        return {
            "table": table,
            "columns": [
                {
                    "name": str(row["name"]),
                    "type": str(row["type"]),
                    "nullable": not bool(row["notnull"]),
                    "primary_key": bool(row["pk"]),
                }
                for row in rows
            ],
        }

    def run_readonly_query(self, sql: str, max_rows: int | None = None) -> dict[str, Any]:
        keyword = self._first_keyword(sql)
        if keyword not in {"select", "with"}:
            raise ValueError("Northstar MCP permits only SELECT or WITH queries")

        row_cap = self.max_rows if max_rows is None else max_rows
        if row_cap < 1 or row_cap > self.max_rows:
            raise ValueError(f"max_rows must be between 1 and {self.max_rows}")

        with self._connect() as con:
            cursor = con.execute(sql)
            columns = [description[0] for description in cursor.description or []]
            fetched = cursor.fetchmany(row_cap + 1)

        truncated = len(fetched) > row_cap
        rows = fetched[:row_cap]
        return {
            "columns": columns,
            "rows": [dict(row) for row in rows],
            "row_count": len(rows),
            "truncated": truncated,
            "max_rows": row_cap,
        }

    @staticmethod
    def get_metric_definition(metric: str) -> dict[str, Any]:
        definitions = {
            "revenue": {
                "name": "revenue",
                "definition": "SUM(revenue)",
                "unit": "dataset currency units",
            },
            "gross_profit": {
                "name": "gross_profit",
                "definition": "SUM(revenue) - SUM(cogs)",
                "unit": "dataset currency units",
            },
            "gross_margin": {
                "name": "gross_margin",
                "definition": "(SUM(revenue) - SUM(cogs)) / SUM(revenue)",
                "unit": "ratio",
            },
        }
        key = metric.strip().lower().replace(" ", "_")
        if key not in definitions:
            raise ValueError(f"Unknown Northstar metric: {metric}")
        return definitions[key]
