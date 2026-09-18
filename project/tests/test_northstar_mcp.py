from __future__ import annotations

import pytest
from mcp import Client

from northstar_mcp.server import mcp
from northstar_mcp.service import NorthstarService


def test_service_blocks_write_sql() -> None:
    service = NorthstarService()
    with pytest.raises(ValueError, match="SELECT or WITH"):
        service.run_readonly_query("DELETE FROM sales")


def test_service_returns_known_q2_revenue() -> None:
    service = NorthstarService()
    result = service.run_readonly_query(
        "SELECT SUM(revenue) AS revenue FROM sales WHERE quarter = 'Q2'"
    )
    assert result["rows"] == [{"revenue": 1070}]


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.mark.anyio
async def test_mcp_lists_course_tools() -> None:
    async with Client(mcp, raise_exceptions=True) as client:
        listing = await client.list_tools()
    names = {tool.name for tool in listing.tools}
    assert names == {
        "get_schema",
        "get_table_info",
        "run_readonly_query",
        "get_metric_definition",
    }


@pytest.mark.anyio
async def test_mcp_schema_and_query_round_trip() -> None:
    async with Client(mcp, raise_exceptions=True) as client:
        schema = await client.call_tool("get_schema", {})
        result = await client.call_tool(
            "run_readonly_query",
            {
                "sql": (
                    "SELECT region, SUM(revenue - cogs) AS gross_profit "
                    "FROM sales WHERE quarter = 'Q2' "
                    "GROUP BY region ORDER BY region"
                )
            },
        )

    assert schema.is_error is False
    assert schema.structured_content is not None
    assert "sales" in schema.structured_content["tables"]

    assert result.is_error is False
    assert result.structured_content is not None
    assert result.structured_content["row_count"] == 3


@pytest.mark.anyio
async def test_mcp_rejects_write_query_as_tool_error() -> None:
    async with Client(mcp, raise_exceptions=True) as client:
        result = await client.call_tool(
            "run_readonly_query",
            {"sql": "UPDATE sales SET revenue = 0"},
        )

    assert result.is_error is True
    assert result.structured_content is None
