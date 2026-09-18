from pathlib import Path
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from sql_harness.adapters.sqlite_adapter import SQLiteReadOnlyAdapter


def test_adapter_blocks_write(tmp_path):
    db = tmp_path / "x.db"
    import sqlite3
    con = sqlite3.connect(db)
    con.execute("create table sales(x integer)")
    con.commit(); con.close()
    a = SQLiteReadOnlyAdapter(db)
    with pytest.raises(PermissionError):
        a.execute_readonly("DELETE FROM sales")
