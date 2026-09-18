# Agentic Analytics Engineering — Curriculum

This file is the canonical Markdown curriculum for the course. The interactive site in `index.html`, the lab specifications in `labs/`, and the through-project in `project/` provide the executable detail.

Each module has **one Study Plan**. Required readings, required code studies, study prompts, and optional Packt enrichment are consolidated there rather than repeated in multiple sections.

The module sequence is deliberate: **Study Plan first → course lesson/concepts → project context → assignment/lab → evidence/self-grade**. Learners should encounter the required sources before comprehension checks or implementation exercises.

## Course goal

Build a production-oriented **self-improving SQL generation agentic harness** while learning how to separate model judgment, deterministic control flow, state, tools, verification, evaluation, persistence, and release governance.

The course is deliberately self-contained:

- all required readings and code studies are available free online;
- the bundled Northstar Retail SQLite database is the course dataset;
- the course's own `northstar_mcp/` server is the **only analytics MCP server used in the course**;
- no pre-existing personal or enterprise analytics MCP server is required or used.

## Through-project architecture

The same Northstar data is accessed through two interchangeable capability paths:

```text
SQL Harness
    |
    +-- SQLiteReadOnlyAdapter ------------------+
    |                                          |
    +-- McpSqlAdapter                           |
            |                                   |
            v                                   |
      Northstar MCP Server                      |
            |                                   |
            +--------------> northstar.db <-----+
```

The purpose is to prove that the harness depends on stable capability contracts rather than transport or implementation details.

At the end of the course, the system must be:

- read-only by construction;
- explicitly stateful;
- verifier-gated;
- evidence-grounded;
- bounded in retries, revisions, and budgets;
- durable and resumable;
- regression-tested;
- capable of proposing improvements through a champion/challenger workflow;
- incapable of silently modifying the production champion.

---

## Module 0 — Architecture & Mental Model

**Duration:** 1.5–2 hours

**Goal:** Distinguish deterministic workflows from autonomous agents and decide exactly where LLM judgment belongs.

**Core topics**

- workflow vs. agent
- prompt chaining
- routing
- parallelization
- orchestrator-worker
- evaluator-optimizer
- control plane vs. agent harness
- durable state vs. model context
- MCP as capability boundary

**Study plan — required/free**

- Anthropic — Scaling Managed Agents
- Claude Platform — Managed Agents overview
- Anthropic — Effective Context Engineering for AI Agents
- Anthropic — Building Effective Agents
- Anthropic `claude-cookbooks/patterns/agents/`
- Anthropic `claude-cookbooks/claude_agent_sdk/`

**Lab**

Inspect the **course-supplied Northstar baseline** in `project/00-baseline.md` and `project/sql_harness/baseline.py`. Classify each meaningful step:

- D = deterministic code
- L = LLM judgment
- T = tool/capability
- S = Skill/domain expertise

Then redesign it as an explicit target architecture. No pre-existing learner system is assumed. The Module 0 worksheet is intentionally blank apart from its column headings; identifying the baseline steps, assigning D/L/T/S ownership, and proposing the target behavior are learner work.

**Architecture decision record (ADR) log**

An ADR is a short record of a consequential design choice, its rationale, and its consequences. The log is intentionally empty at the start of the course. Learners add an ADR only when a lab produces a real architecture choice worth preserving and revisiting; later evidence may reject or supersede it. Routine implementation details do not need ADRs.

**Through-project milestone**

Freeze the supplied baseline and architecture for later comparison.

**Artifacts**

- `project/baseline/`
- `architecture-v0.md`

---

## Module 1 — Core Agent Patterns from First Principles

**Duration:** 3–4 hours

**Goal:** Implement the foundational control-flow patterns before using an agent framework.

**Core topics**

- single-shot routing
- ReAct/tool loops
- planner-executor
- reflection
- verifier gates
- stop conditions
- structured traces

**Study plan — required/free**

- DeepLearning.AI — AI Agents in LangGraph / agent-from-scratch material
- public Packt Chapter 5 and Chapter 7 companion code
- Anthropic `patterns/agents/basic_workflows.ipynb`
- Anthropic `patterns/agents/evaluator_optimizer.ipynb`

**Programming lab**

Implement five patterns without LangChain, LangGraph, CrewAI, AutoGen, or another agent framework.

**Through-project milestone**

Add reusable SQL-harness primitives in `project/sql_harness/patterns.py`.

Important course boundary: use only the bundled Northstar SQLite database and fake/mock tools here. The Northstar MCP server is introduced in Module 4.

---

## Module 2 — State, Schemas & Control Flow

**Duration:** 2–2.5 hours

**Goal:** Replace implicit conversational context with explicit, typed, serializable application state.

**Core topics**

- Pydantic/dataclass state models
- reducers
- validation
- messages vs. durable state
- deterministic merge behavior
- state serialization

**Study plan — required/free**

- LangChain Academy — Introduction to LangGraph
- LangGraph Graph API
- Packt Chapter 2 free chapter

**Programming lab**

Define typed analysis state, deterministic reducer behavior, validation, and JSON round trips.

**Through-project milestone**

Create `project/sql_harness/models.py` with typed request, schema context, SQL candidate, verification, result, claim, metrics, harness state, and configuration-version objects.

---

## Module 3 — Routing, Parallelism & Orchestration

**Duration:** 2–3 hours

**Goal:** Build explicit graphs and use them for routing, fan-out/fan-in, candidate generation, verification, and repair.

**Core topics**

- routing
- parallel nodes
- fan-out/fan-in
- map-reduce
- orchestrator-worker
- explicit graph edges
- bounded repair

**Study plan — required/free**

- LangGraph workflow-pattern material
- Anthropic `patterns/agents/orchestrator_workers.ipynb`
- Anthropic `claude_agent_sdk/08_Dynamic_workflows.ipynb`
- public Packt Chapter 7 code

**Programming lab**

Build router, fan-out/fan-in, and orchestrator-worker graphs against Northstar.

**Through-project milestone**

Create the SQL control graph:

```text
request
  -> route
  -> schema_context
  -> generate_sql
  -> verify_sql
  -> execute
  -> verify_result
  -> finalize
```

Include clarification, bounded repair, and optional candidate fan-out.

---

## Module 4 — MCP, Skills & Workflow Boundaries

**Duration:** 1–1.5 hours

**Goal:** Make the capability boundary explicit and prove that orchestration code does not depend on SQLite or MCP implementation details.

**Core topics**

- MCP host/client/server
- tools/resources/prompts
- Skills vs. capabilities
- adapter contracts
- defense in depth
- typed capability errors

**Study plan — required/free**

- Hugging Face MCP course — architecture and capabilities
- Anthropic `claude_agent_sdk/02_The_observability_agent.ipynb`
- Anthropic `claude_agent_sdk/03_The_site_reliability_agent.ipynb`
- public Packt Chapter 7 tool/orchestration code

**Programming lab**

Build two interchangeable Northstar access paths:

1. direct `SQLiteReadOnlyAdapter`
2. `McpSqlAdapter` talking to the course-supplied `northstar_mcp/` server

No external analytics MCP server is used.

**Northstar MCP tools**

- `get_schema()`
- `get_table_info(table)`
- `run_readonly_query(sql, max_rows=200)`
- `get_metric_definition(metric)`

**Through-project milestone**

Add capability adapters and contract tests so changing transport requires configuration only.

---

## Module 5 — Planning & Task Decomposition

**Duration:** 2–3 hours

**Goal:** Treat planning as an inspectable artifact and separate semantic planning from deterministic validation.

**Core topics**

- structured planning
- task IDs and dependencies
- plan validation
- ambiguity handling
- malformed structured output
- one-replan policy
- capability availability

**Study plan — required/free**

- Anthropic `claude_agent_sdk/01_The_chief_of_staff_agent.ipynb`
- Anthropic `patterns/agents/orchestrator_workers.ipynb`
- public Packt Chapter 5 planning code
- public Packt Chapter 9 structured-output failure study

**Programming lab**

Implement plan schemas, validators, cycle detection, missing-dependency detection, capability validation, and explicit parse failures.

**Through-project milestone**

Create `project/sql_harness/planner.py` for multi-query questions while bypassing planning for simple lookups.

---

## Module 6 — Evaluator, Critic, Verifier & Revision Loops

**Duration:** 2–3 hours

**Goal:** Separate usefulness/quality critique from correctness verification.

**Core topics**

- evaluator-optimizer
- deterministic verification
- claim grounding
- conflict detection
- structured repair feedback
- bounded revision
- escalation

**Study plan — required/free**

- Anthropic `patterns/agents/evaluator_optimizer.ipynb`
- Anthropic `claude_agent_sdk/08_Dynamic_workflows.ipynb`
- Andrew Ng reflection material
- public Packt Chapter 8/9 code

**Programming lab**

Implement:

- analysis critic
- visualization critic
- numeric verifier
- evidence grounding verifier
- conflict/escalation path
- bounded generate → verify → critique → revise loop

**Through-project milestone**

Add three distinct SQL-harness gates:

1. pre-execution SQL verifier
2. result verifier
3. claim/evidence verifier

A hard verifier failure cannot be overridden by critic opinion.

---

## Module 7 — End-to-End Analytics Vertical Slice

**Duration:** 3–4 hours

**Goal:** Run one evidence-grounded analytical workflow end to end and prove adapter portability.

**Study plan — required/free**

- Phoenix talk-to-data material
- public Packt Chapter 8 data analysis / V&V / tri-agent code
- Anthropic `capabilities/text_to_sql/guide.ipynb`

**Required question**

> Why did gross margin fall from Q1 to Q2, and which region contributed most?

**Known Northstar truth**

- Q1 gross margin = 41.8%
- Q2 gross margin ≈ 35.98%
- change ≈ -5.82 percentage points
- West gross profit = 178 → 148, a decline of 30 dataset units
- West is the largest negative contributor

**Required experiment**

Run the same harness, same question, and same underlying Northstar data twice:

1. `SQLiteReadOnlyAdapter` → `northstar.db`
2. `McpSqlAdapter` → course `Northstar MCP Server` → `northstar.db`

Only the capability adapter changes.

**Through-project milestone**

Produce structured plan, schema context, SQL attempts, verification records, evidence-bearing query results, final claims, answer, visualization spec, and full trace for both runs.

---

## Module 8 — Persistence, Retries & Human Intervention

**Duration:** 2–3 hours

**Goal:** Make runs durable and prove failure semantics under deterministic injected faults.

**Core topics**

- checkpoints
- resumable sessions
- idempotency
- retry taxonomy
- HITL interrupts
- durable state vs. transcript
- terminal failure states

**Study plan — required/free**

- LangGraph persistence/HITL
- Anthropic `claude_agent_sdk/05_Building_a_session_browser.ipynb`
- public Packt Chapter 7 workflow/state-machine examples

**Failure drills**

- timeout twice, succeed on third attempt
- ambiguity interrupt/resume
- process crash after completed work
- critique-driven reanalysis
- confidence threshold triggering HITL

**Through-project milestone**

Create `project/sql_harness/persistence.py` and prove resumed runs do not duplicate completed SQL execution.

---

## Module 9 — Multi-Agent vs. Workflow

**Duration:** 2–3 hours

**Goal:** Evaluate multi-agent collaboration empirically instead of assuming it is better.

**Study plan — required/free**

- CrewAI docs
- DeepLearning.AI CrewAI course
- public Packt Chapter 7 manager/orchestration code

**Experiment**

Compare the existing workflow implementation against a CrewAI variant using the same Northstar cases, data, verification rules, and model settings.

Measure:

- correctness
- unsafe-query block rate
- model calls
- tool calls
- latency
- token/cost usage
- trace clarity

**Through-project milestone**

Write an evidence-based `project/multi_agent_decision.md`.

---

## Module 10 — Evaluations & Observability

**Duration:** 3–4 hours

**Goal:** Build a frozen regression suite that measures nodes, trajectories, and outcomes separately.

**Study plan — required/free**

- DeepLearning.AI — Evaluating AI Agents
- Anthropic eval guidance
- Anthropic `capabilities/text_to_sql/evaluation/`
- Anthropic `evals/agentic_search/reproduce_agentic_search_benchmarks.ipynb`
- public Packt Chapter 9 self-improvement code

**Benchmark**

Expand to at least 25 cases spanning:

- lookup
- aggregation
- derived metrics
- comparison
- diagnostic/multi-step
- ambiguity
- unknown schema
- unsafe write
- prompt-injection-like data/context
- empty-result cases

**Required graders**

- deterministic SQL-safety grader
- result-equivalence grader
- claim-grounding grader
- selected route/trajectory assertions
- optional model-based usefulness grader

**Through-project milestone**

Create `project/sql_harness/evals.py` and version the frozen benchmark before any self-improvement work begins.

---

## Module 11 — Production Engineering & Safe Self-Improvement

**Duration:** 3–4 hours

**Goal:** Make the harness fail safely and introduce controlled champion/challenger improvement.

**Core topics**

- chaos testing
- budgets
- rollback
- prompt injection
- malformed tool output
- unavailable capabilities
- checkpoint corruption
- bounded unattended execution
- release gates

**Study plan — required/free**

- Anthropic trustworthy/reliability material
- Anthropic `claude_agent_sdk/03_The_site_reliability_agent.ipynb`
- Anthropic `claude_agent_sdk/07_Hosting_the_agent.ipynb`
- public Packt Chapter 9 safeguard/self-improvement code

**Chaos matrix**

Include at least:

- MCP timeout
- malformed tool JSON
- unavailable capability
- prompt injection in metadata
- oversized query result
- duplicate retry/idempotency
- parallel worker failure
- contradictory critic verdicts
- budget exhaustion
- corrupt checkpoint

**Self-improvement loop**

```text
runs
 -> failure clustering
 -> proposal
 -> approval
 -> challenger config
 -> benchmark
 -> promote/reject
 -> audit log
```

The champion never edits itself in place.

**Through-project milestone**

Create `project/sql_harness/improvement.py` with versioned configuration objects, benchmark evidence, approval records, promotion gates, and exact rollback.

---

## Module 12 — Capstone

**Duration:** 3–5 hours

**Goal:** Demonstrate whether the engineered harness improves reliability enough to justify its added complexity.

**Study A — baseline vs. final**

Run the frozen Module 0 baseline and final system on the exact same benchmark.

Compare:

- correctness
- unsupported-claim rate
- verifier catches
- tool/model calls
- latency
- token/cost usage
- convergence iterations

**Study B — one complete improvement cycle**

1. choose a real failure cluster;
2. generate an improvement proposal;
3. approve it for experiment;
4. build a challenger configuration;
5. run the full benchmark;
6. promote or reject using Module 11 gates.

**Final deliverables**

- `capstone/CAPSTONE.md`
- baseline and final result sets
- representative traces
- final architecture
- safety/reliability analysis
- latency/cost tradeoff
- champion/challenger history
- rollback demonstration
- explicit list of what was deliberately **not** agentified

---

# Course-wide rules

1. **Northstar only for analytics MCP.** The course does not use any personal or enterprise analytics MCP server.
2. **MCP is a capability layer, not the outer orchestrator.**
3. **LLM judgment is bounded by deterministic lifecycle control.**
4. **State is explicit and durable; chat transcripts are not the application database.**
5. **Verification and critique are different mechanisms.**
6. **Unsafe SQL never reaches execution.**
7. **Every settled numeric claim is evidence-grounded.**
8. **Retries, replans, and revisions have code-owned limits.**
9. **Evaluation precedes promotion.**
10. **Self-improvement means propose → benchmark → approve/promote or reject/rollback, never silent production self-modification.**

# Free-source policy

Every required lesson, source study, lab, self-grade, and capstone requirement can be completed with free online material. Paid Packt chapters remain optional enrichment. The public Packt companion repository and Anthropic cookbooks may be required where indicated.

See:

- `ANTHROPIC_CODE_MAP.md`
- `BOOK_MAP.md`
- `PACKT_CODE_INDEX.md`
- `PACKT_CODE_REVIEW.md`
- `project/PROJECT_SPEC.md`
- `project/MILESTONES.md`
