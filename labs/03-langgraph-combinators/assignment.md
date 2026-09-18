# Module 3: LangGraph Routing + Fan-out/Fan-in Lab

Implement three workflow combinators in LangGraph and observe how explicit state/edges replace hand-written loop control.

## Source study / code archaeology
1. FREE source study: inspect `ManagerAgent` and `workflow_manager_agent` in the public Chapter 7 simulation notebook and review the required LangGraph routing/parallelization lesson. Optional book deep dive: Ch. 7 pp. 186–200.
2. Extract three ideas only: specialist delegation, shared/aggregated state, and guard/HITL transitions. Re-express those as LangGraph nodes/edges rather than copying the classes.
3. In SOURCE_NOTES.md, identify one behavior in the Packt manager that should remain agentic and one that should become deterministic graph control in our analytics system.

## Tasks
1. Graph A Router: route lookup, diagnostic, and report requests to three different nodes from a structured RouteDecision.
2. Graph B Fan-out/Fan-in: dispatch West, East, and Central margin analysis workers and aggregate their TaskResults into one state.
3. Graph C Orchestrator-worker: planner dynamically selects 2–5 analysis workers for ‘Why did gross margin decline from Q1 to Q2?’ and aggregate only after all selected workers complete.
4. Emit a trace containing node name, start/end time, input state keys, and output state keys.

## Fixed scenario / inputs
- Use Northstar Retail data only.
- Reference answer: total gross margin falls from 41.8% in Q1 to about 35.98% in Q2; West has the largest gross-profit decline (-30 in dataset units).

## Constraints
- LangGraph required
- Workers receive task-scoped context
- Aggregation must use structured results, not concatenated chat transcripts

## Acceptance tests
- [ ] Each of the three routes executes exactly one specialized branch
- [ ] Fan-out produces exactly three worker results before aggregation
- [ ] Orchestrator emits between 2 and 5 tasks
- [ ] Final diagnostic identifies West as the largest negative gross-profit contributor
- [ ] Trace proves aggregate happens after workers

## Deliverables
- `graphs.py`
- `test_graphs.py`
- `graph-trace.json`
- `graph-diagram.md`

## Required Anthropic cookbook study

- `claude_agent_sdk/08_Dynamic_workflows.ipynb`: answer the notebook's central architectural question for our SQL harness: **who should hold the plan, model context or deterministic workflow code?**
- Inspect `agent()`, `parallel()`, `pipeline()`, phases, and structured outputs. Map each to one LangGraph construct before coding.

## Through-project milestone — SQL Harness M3: Explicit Graph

Build `project/sql_harness/graph.py` as the first real control plane.

### Required graph
`request → route → schema_context → generate_sql → verify_sql → execute → verify_result → finalize`

Add:
- clarification branch;
- repair edge from failed verification back to generation;
- maximum SQL attempts = 3;
- candidate fan-out experiment: generate 2 candidates in parallel, deterministically select only among candidates that pass verification.

### Acceptance
- Execution node is unreachable unless verification status is PASS.
- Repair never exceeds 3 total candidates.
- Fan-in waits for both candidate branches.
- Trace records node order and state keys changed.
- One test proves a verifier rejection cannot be bypassed by graph routing.
