# Module 5: Structured Planner + Validator Lab

Make planning an inspectable artifact and separate semantic planning from deterministic plan validation.

## Source study / code archaeology
1. FREE source study: inspect the public Chapter 5 Planning Agent/dependency execution and Anthropic orchestrator-worker material. Explain how dependency-aware execution differs from asking an LLM to narrate a plan. Optional book deep dive: Ch. 5 pp. 131–137.
2. Inspect the Chapter 9 LLM_COMPARISON structured-output failure: cloud providers fail PlannerAgent JSON parsing. Treat this as a design requirement, not an anecdote.
3. Write PLANNER_CONTRACT.md before coding: exact JSON schema, failure behavior, single-replan rule, and what must NEVER be silently repaired.

## Tasks
1. Implement AnalysisPlan and AnalysisTask schemas with objective, success_criteria, task IDs, dependencies, required_capabilities, and parallelizable flag.
2. Planner must return schema-valid JSON for the 10 supplied business questions.
3. Implement validate_plan(): detect duplicate IDs, missing dependencies, cycles, no terminal task, and unavailable capabilities.
4. If validation fails, allow exactly one replan using a machine-generated validation error summary.
5. Do not execute any analysis in this module.
6. Structured-output hardening: feed the planner (a) valid JSON, (b) JSON wrapped in markdown fences, (c) missing required fields, and (d) syntactically invalid JSON. Only case (a) may proceed directly; all others must produce explicit validation/parse errors and at most one replan.

## Fixed scenario / inputs
- Cases include simple lookup, root-cause analysis, visualization request, ambiguous request, impossible capability, and intentionally over-broad request.
- A simple lookup should not become a 10-task plan.

## Constraints
- Planner is LLM-driven or mockable
- Validator is deterministic code
- Maximum replans = 1

## Acceptance tests
- [ ] All valid plans pass schema validation
- [ ] Cycle fixture is rejected
- [ ] Missing dependency fixture is rejected
- [ ] Unavailable-capability fixture is rejected
- [ ] Simple lookup uses <=2 tasks
- [ ] Ambiguous case explicitly requests clarification or records an ambiguity
- [ ] Markdown-wrapped/malformed planner output never silently becomes an executable plan

## Deliverables
- `planner.py`
- `plan_models.py`
- `plan_validator.py`
- `planner_cases.jsonl`
- `planner_results.json`
- `PLANNER_CONTRACT.md`
- `SOURCE_NOTES.md`

## Required Anthropic cookbook study

- `claude_agent_sdk/01_The_chief_of_staff_agent.ipynb`: inspect Plan Mode, subagents, persistent instructions, and hooks. Write one paragraph distinguishing a planning artifact from authority to execute it.
- Compare with `patterns/agents/orchestrator_workers.ipynb` and list two differences between the minimal pattern and the newer SDK-oriented implementation.

## Through-project milestone — SQL Harness M5: Query Planning

Add `project/sql_harness/planner.py` for questions that require more than one SQL operation.

### Fixed cases
- Simple lookup: “What was Q2 revenue?” → **no multi-step plan**.
- Comparison: “How did gross margin change from Q1 to Q2?” → plan may contain separate evidence tasks.
- Diagnostic: “Why did gross margin fall, and which region contributed most?” → 2–5 tasks with dependencies.
- Ambiguous: “How are we doing?” → clarification, not invented intent.

### Acceptance
- Planner emits schema-valid `SqlAnalysisPlan`.
- Validator rejects missing dependencies/cycles/unavailable capabilities.
- One replan maximum.
- Markdown-fenced or malformed planner JSON is never silently executed.
- Router bypasses planner for simple lookup cases.
