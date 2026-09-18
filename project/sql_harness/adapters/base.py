from __future__ import annotations
from typing import Protocol, Any


class SchemaProvider(Protocol):
    def get_schema(self, request: str) -> Any:
        """Return schema/context needed for a request."""
        ...


class SqlExecutor(Protocol):
    def execute_readonly(self, sql: str) -> Any:
        """Execute an already-verified read-only SQL statement."""
        ...
