# Module 9: CrewAI vs Workflow Controlled Experiment

Evaluate multi-agent collaboration empirically rather than assuming more agents are better.

## Tasks
1. Implement the same Northstar diagnostic in Version A using your LangGraph planner/workers and Version B using a CrewAI Flow/Crew with region/data specialists.
2. Run each version 5 times on the same model/settings.
3. Record answer correctness, number of model calls, tool calls, wall time, tokens/cost if available, and trace complexity.
4. Write a decision memo: keep, restrict, or remove the multi-agent approach for this use case.

## Fixed scenario / inputs
- Both versions must use the same capability adapter and final verification rules.

## Constraints
- Do not change the question between variants
- Do not give one variant extra source data
- Decision must cite measured results

## Acceptance tests
- [ ] 10 total runs recorded
- [ ] Both variants pass numeric verifier or failures are counted
- [ ] Comparison table includes all required metrics
- [ ] Decision memo identifies at least two benefits and two costs
- [ ] Architecture decision log updated with the result

## Deliverables
- `comparison_runs.csv`
- `crewai_variant/`
- `langgraph_variant/`
- `framework-decision.md`

## Through-project milestone — SQL Harness M9: Multi-Agent Experiment

Do **not** automatically convert the SQL harness to multi-agent.

### Experiment
Rebuild only the candidate-generation/verification segment using CrewAI (or a Crew + Flow):
- SQL generator specialist;
- SQL verifier specialist;
- coordinator/Flow.

Run the same 10 benchmark cases through:
A. existing LangGraph/control-plane implementation;
B. CrewAI variant.

### Measure
- result correctness;
- unsafe-query block rate;
- tool/model calls;
- latency;
- tokens/cost;
- trace clarity.

### Acceptance
Write `project/multi_agent_decision.md` with a KEEP / REJECT / USE ONLY FOR ___ decision backed by measurements. No framework preference by aesthetics.
