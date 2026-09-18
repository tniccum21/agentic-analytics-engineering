# Module 4: MCP Boundary + Adapter Lab

Prove that orchestration code can depend on stable capability interfaces rather than MCP implementation details.

## Study evidence

Complete the module's single **Study Plan** in the course site first. This section is not an additional reading list; it specifies the observations and artifacts to capture from those sources.

- `claude_agent_sdk/02_The_observability_agent.ipynb`: trace how MCP tools are exposed and invoked.
- `claude_agent_sdk/03_The_site_reliability_agent.ipynb`: inspect pre-tool safety hooks and write validation. Record which protections belong at the capability boundary even if the harness also has an upstream verifier.

## Tasks
1. Create AnalyticsCapabilities with get_schema(table), run_readonly_query(sql), and render_chart(spec).
2. Implement LocalNorthstarAdapter against the bundled SQLite data.
3. Implement MCPAnalyticsAdapter against the **course-supplied Northstar MCP server**, normalizing tool outputs/errors to the same local interface.
4. Classify 12 supplied concerns as control plane, agent harness, MCP/tool, resource/context, or Skill.
5. Run the same analysis function against the local adapter and MCP adapter without changing analysis code.

## Fixed scenario / inputs
- retry count, max revisions, task scheduling, and checkpoint policy are NOT allowed inside the adapter
- Tool errors must normalize to a typed CapabilityError

## Constraints
- The analysis function may import only the interface/protocol, not an MCP SDK
- No framework-specific types in the capability contract

## Acceptance tests
- [ ] Local adapter passes conformance tests
- [ ] MCP adapter has the same public method signatures
- [ ] Switching adapters requires configuration only
- [ ] No retry/loop policy appears in adapter code
- [ ] CapabilityError includes tool name and original cause

## Deliverables
- `capabilities.py`
- `local_adapter.py`
- `mcp_adapter.py`
- `boundary-classification.md`
- `test_capabilities.py`


## Through-project milestone — SQL Harness M4: Replaceable Hands

Create capability adapters so the harness does not know whether Northstar SQL runs directly through SQLite or through the course's MCP boundary.

### Required implementation
1. Keep `SQLiteReadOnlyAdapter` behind `SchemaProvider` and `SqlExecutor` interfaces.
2. Add `McpSqlAdapter` with the same interfaces and connect it to the **course-supplied Northstar MCP server**. Unit tests may use the official SDK's in-memory client; no external MCP server is needed.
3. Add an adapter contract test suite that runs against both implementations/mocks.
4. Schema discovery must return structured context rather than a raw prompt blob.
5. Execution must return a structured `QueryResult`.

### Acceptance
- Graph code imports protocols/interfaces, not SQLite or MCP implementation details.
- Switching adapter requires configuration only.
- Read-only enforcement exists in both verifier and adapter (defense in depth).
- MCP errors are normalized into typed capability errors.
