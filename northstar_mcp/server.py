from __future__ import annotations

from typing import Any

from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError
from mcp.types import ToolAnnotations

from .service import NorthstarService

service = NorthstarService()
mcp = MCPServer(
    "Northstar Retail",
    instructions=(
        "Read-only course server for the bundled Northstar Retail dataset. "
        "Use schema tools before querying. All SQL execution is read-only."
    ),
)

_READ_ONLY = ToolAnnotations(read_only_hint=True, open_world_hint=False)


@mcp.tool(
    title="Get Northstar schema",
    annotations=_READ_ONLY,
)
def get_schema() -> dict[str, Any]:
    """Return the structured schema for the bundled Northstar Retail database."""
    return service.get_schema()


@mcp.tool(
    title="Get Northstar table information",
    annotations=_READ_ONLY,
)
def get_table_info(table: str) -> dict[str, Any]:
    """Return column metadata for one Northstar table."""
    try:
        return service.get_table_info(table)
    except ValueError as exc:
        raise ToolError(str(exc)) from exc


@mcp.tool(
    title="Run read-only Northstar SQL",
    annotations=_READ_ONLY,
)
def run_readonly_query(sql: str, max_rows: int = 200) -> dict[str, Any]:
    """Execute a SELECT/CTE query with a server-side result-row cap."""
    try:
        return service.run_readonly_query(sql, max_rows=max_rows)
    except (ValueError, sqlite3.Error) as exc:  # type: ignore[name-defined]
        raise ToolError(str(exc)) from exc


@mcp.tool(
    title="Get Northstar metric definition",
    annotations=_READ_ONLY,
)
def get_metric_definition(metric: str) -> dict[str, Any]:
    """Return the canonical definition for a course metric."""
    try:
        return service.get_metric_definition(metric)
    except ValueError as exc:
        raise ToolError(str(exc)) from exc


def main() -> None:
    """Run the course server over stdio."""
    mcp.run()


if __name__ == "__main__":
    main()
