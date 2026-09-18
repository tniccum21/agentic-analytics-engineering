# Northstar MCP Server

This is the **only analytics MCP server used by the course**.

It exposes the bundled Northstar Retail SQLite database through a deliberately small, read-only MCP surface. The goal is to make MCP a reproducible course dependency rather than relying on any learner's personal or enterprise infrastructure.

## Tools

- `get_schema()`
- `get_table_info(table)`
- `run_readonly_query(sql, max_rows=200)`
- `get_metric_definition(metric)`

The service opens SQLite in `mode=ro`, enables `PRAGMA query_only`, accepts only `SELECT`/CTE entry points, and caps returned rows. The SQL harness still adds its own upstream verifier later in the course. That duplication is intentional defense in depth.

## SDK version

The server uses the current stable **MCP Python SDK v2** API:

```python
from mcp.server import MCPServer
```

MCP Python SDK v2 became the stable line in July 2026.

## Install

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

## Test without a subprocess

The official SDK supports an in-memory client, which is what the course tests use:

```python
from mcp import Client
from northstar_mcp.server import mcp

async with Client(mcp) as client:
    result = await client.call_tool("get_schema", {})
```

## Run with stdio

```bash
python -m northstar_mcp.server
```

or with the SDK CLI:

```bash
mcp dev northstar_mcp/server.py
```

For the course, stdio is the canonical transport. Streamable HTTP is a later deployment concern, not required for the labs.

## Course progression

- Modules 0–3 use the direct SQLite adapter so control flow is easy to see.
- Module 4 introduces this server and the `McpSqlAdapter`.
- Module 7 runs the **same Northstar question against the same Northstar data twice**: once via direct SQLite, once via MCP.
- Later modules keep the MCP boundary available while adding persistence, evals, and controlled self-improvement.

No external analytics MCP server is used anywhere in the course.
