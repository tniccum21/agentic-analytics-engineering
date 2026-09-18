# Module 1: Pattern Atlas Programming Lab

Implement five distinct agent control-flow patterns against one fixed analytics scenario so you can recognize what a framework is doing later.

## Study evidence

Complete the module's single **Study Plan** in the course site first. This section is not an additional reading list; it specifies the observations and artifacts to capture from those sources.
1. FREE code archaeology: inspect the public Chapter 5 simulation notebook (`ch05_foundational_architectures__RUN_NO_KEY_SIMULATION.ipynb`). Identify where task dependencies are represented and where code, not the model, controls readiness/termination. Optional book deep dive: Ch. 5 pp. 118–135.
2. Inspect Chapter 7 data_viz_agent. In SOURCE_NOTES.md, diagram its Think → Plan → Act → data_state flow and label each transition M (model), C (control code), or T (tool).
3. Before implementing your five patterns, write a 5-row comparison predicting how their traces should differ. After implementation, revise the table using actual traces.


### Additional code-study prompts

- `patterns/agents/basic_workflows.ipynb`: identify prompt chaining, routing, and parallelization; mark which transitions are code-owned and model-owned.
- `patterns/agents/evaluator_optimizer.ipynb`: preview the generate/evaluate/revise loop and record its explicit exit condition.

## Tasks
1. 1A — Single-shot router: implement single_shot_route(request, model). It must make exactly one model call, make zero tool calls, and return one of lookup | analysis | visualization | unsupported plus a short rationale.
2. 1B — ReAct/tool loop: implement react_agent(goal, model, tools, max_steps=4). Each iteration must record action, tool input, observation, and step number. Unknown tools become an error observation rather than an exception. Stop on a final response or at step 4.
3. 1C — Planner–executor: implement planner_executor(goal, planner, executors). The planner must emit structured tasks with IDs and dependencies. The executor must not execute a task until dependencies are complete. Planning and execution are separate callables.
4. 1D — Reflexive agent: implement reflexive_agent(request, generator, critic, max_revisions=2). The critic returns {verdict, issues, required_changes}; revision receives the previous artifact plus that critique. No more than two revisions.
5. 1E — Verifier-gated agent: implement verifier_gated(proposal, verifier, tools). The verifier runs BEFORE the action. A rejected proposal must result in zero tool executions; an approved proposal may execute exactly once.

## Fixed scenario / inputs
- Use the bundled Northstar Retail SQLite database and mock tools. Do not connect to the course Northstar MCP server yet; MCP is introduced in Module 4.
- ReAct goal: ‘Which region had the largest decline in gross profit from Q1 to Q2, and by how much?’
- Planner–executor goal: ‘Explain why gross margin declined from Q1 to Q2.’
- Reflection fixture: a draft executive summary containing one unsupported causal claim.
- Verifier cases: SELECT-only analytics query must pass; DELETE/UPDATE or a query without a row limit must fail.

## Constraints
- Python 3.11+
- No LangChain, LangGraph, CrewAI, AutoGen, or other agent framework
- No hidden recursive calls
- All loop budgets are constants/arguments owned by code, not chosen by the model
- Every pattern returns an execution trace

## Acceptance tests
- [ ] test_single_shot_calls_model_once passes
- [ ] test_react_executes_tools_and_stops passes
- [ ] test_react_hard_stops_at_four_steps passes
- [ ] test_planner_respects_dependencies passes
- [ ] test_reflexive_never_exceeds_two_revisions passes
- [ ] test_verifier_prevents_rejected_tool_call passes
- [ ] test_verifier_allows_approved_tool_call_once passes

## Deliverables
- `patterns.py`
- `test_patterns.py (do not modify the supplied assertions except to add tests)`
- `trace_examples.json containing one successful trace for each pattern`
- `PATTERN_NOTES.md: 1–2 sentences on when you would and would not use each pattern`


## Through-project milestone — SQL Harness M1: Pattern Primitives

Apply the five patterns to the SQL harness, not only the generic Northstar exercises.

### Required implementation
1. Add `project/sql_harness/patterns.py`.
2. Implement `single_shot_sql_route(question, model)` returning `lookup | sql | clarify | unsupported`.
3. Implement `sql_react_loop(question, model, schema_tool, sql_tool, max_steps=4)` **using a fake executor only** in this module; record every action/observation.
4. Implement `sql_planner_executor(question, planner, executor)` with task IDs/dependencies for a two-query comparison question.
5. Implement `sql_reflexive_generate(question, generator, critic, max_revisions=2)` for SQL candidate repair.
6. Implement `sql_verifier_gate(candidate, verifier, executor)` and prove a write query produces zero executor calls.

### Acceptance
- Five project primitives produce distinct structured traces.
- `DELETE`, `UPDATE`, `INSERT`, and `DROP` fixtures cannot reach the executor.
- All loop/revision budgets are code-owned constants/arguments.
- Add `project/tests/test_patterns.py`.
