# Anthropic Claude Cookbooks — Course Map

The public `anthropics/claude-cookbooks` repository is a major free-code backbone of this course.

## Two strata

### Minimal pattern notebooks
`patterns/agents/`

Use these to see control flow without a large harness:
- `basic_workflows.ipynb` — chaining, routing, parallelization
- `orchestrator_workers.ipynb` — dynamic decomposition + workers
- `evaluator_optimizer.ipynb` — bounded generation/evaluation/revision
- `async_multi_agent_orchestration.ipynb` — async multi-agent orchestration

These accompany older *Building Effective Agents* material. We use them as minimal pattern references, not as the full current Anthropic harness architecture.

### Current Agent SDK recipes
`claude_agent_sdk/`

Use these for modern harness/operational ideas:
- `01_The_chief_of_staff_agent.ipynb` — Plan Mode, hooks, subagents, persistent instructions
- `02_The_observability_agent.ipynb` — MCP integrations/tool surfaces
- `03_The_site_reliability_agent.ipynb` — read/write remediation, safety hooks, verify-after-action
- `05_Building_a_session_browser.ipynb` — sessions, history, replay, fork, resume
- `07_Hosting_the_agent.ipynb` — Docker → managed serverless → Kubernetes
- `08_Dynamic_workflows.ipynb` — model-held plans vs deterministic scripts, fan-out/pipelines, structured outputs, adversarial verification

## SQL-specific backbone

`capabilities/text_to_sql/`

- `guide.ipynb` — text-to-SQL implementation, context/RAG, iterative improvement
- `data/` — reproducible examples
- `evaluation/` — Promptfoo evaluation configuration and test cases

This is the closest free Anthropic reference to the course through-project. We do **not** copy it wholesale; we place the useful ideas behind our typed state, replaceable adapters, hard SQL verifier, claim grounding, regression suite, and champion/challenger promotion gates.

## Evaluation example

`evals/agentic_search/reproduce_agentic_search_benchmarks.ipynb`

We use this as an example of packaging a reproducible benchmark, not as a SQL lesson.

## Course mapping

| Module | Required Anthropic code |
|---|---|
| 0 | Agent SDK README + `patterns/agents/` map |
| 1 | `basic_workflows.ipynb`, preview `evaluator_optimizer.ipynb` |
| 3 | `08_Dynamic_workflows.ipynb` |
| 4 | `02_The_observability_agent.ipynb`, `03_The_site_reliability_agent.ipynb` |
| 5 | `01_The_chief_of_staff_agent.ipynb`, `orchestrator_workers.ipynb` |
| 6 | `evaluator_optimizer.ipynb`, verification sections of `08_Dynamic_workflows.ipynb` |
| 7 | `capabilities/text_to_sql/guide.ipynb` |
| 8 | `05_Building_a_session_browser.ipynb` |
| 10 | `capabilities/text_to_sql/evaluation/`, agentic-search benchmark notebook |
| 11 | `03_The_site_reliability_agent.ipynb`, `07_Hosting_the_agent.ipynb` |
| 12 | revisit Dynamic Workflows + Text-to-SQL as architecture/eval cross-checks |
