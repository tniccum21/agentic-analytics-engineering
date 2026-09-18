from pathlib import Path
import sqlite3

DB = Path(__file__).with_name("northstar.db")

def run_sql(sql: str):
    q = sql.strip()
    if not q.lower().startswith("select"):
        raise PermissionError("Northstar lab tool is read-only")
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    try:
        return [dict(r) for r in con.execute(q).fetchall()]
    finally:
        con.close()

def gross_margin(quarter: str, region: str | None = None):
    where = "quarter = ?" + (" AND region = ?" if region else "")
    args = [quarter] + ([region] if region else [])
    row = _query(where, args)[0]
    return (row["revenue"] - row["cogs"]) / row["revenue"]

def _query(where,args):
    con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
    try: return [dict(r) for r in con.execute(f"SELECT SUM(revenue) revenue, SUM(cogs) cogs FROM sales WHERE {where}",args).fetchall()]
    finally: con.close()
