# Module 10: 25-Case Agent Evaluation Suite

Create regression tests that measure nodes, trajectories, and final outcomes separately.

## Study evidence

Complete the module's single **Study Plan** in the course site first. This section is not an additional reading list; it specifies the observations and artifacts to capture from those sources.
1. FREE source study: complete the required evaluation material and inspect public `chapter09/self_improving.py`. Treat sensing → critic → planner → learning as a CHANGE-PROPOSAL loop, not permission to self-modify production automatically. Optional book deep dive: Ch. 9 pp. 265–277.
2. Inspect chapter09/LLM_COMPARISON.md. Record the structured-output parsing failure as a regression test candidate.
3. Define PROMOTION_POLICY.md before modifying prompts: which benchmark metrics may regress by zero, which have tolerances, and what triggers rollback.


### Additional code-study prompts

- `capabilities/text_to_sql/evaluation/`: inspect the Promptfoo configuration, test inputs, expected outputs, and result workflow.
- `evals/agentic_search/reproduce_agentic_search_benchmarks.ipynb`: inspect the mechanics of reproducible benchmark runs. Borrow the experimental discipline, not the search-specific task.

## Tasks
1. Create 25 cases: 5 numeric known-answer, 5 routing/tool-choice, 5 ambiguous/clarification, 5 injected-failure, 5 visualization/quality cases.
2. For each case define required evidence, expected facts/ranges, forbidden claims/actions, and allowed trajectory flexibility.
3. Implement at least three deterministic graders and one model-based grader.
4. Produce per-case results plus aggregate metrics.
5. Establish a baseline before changing any prompts/architecture.
6. Propose exactly one prompt/Skill/planner change using baseline failures. Re-run all cases. Promote only if PROMOTION_POLICY.md passes; otherwise record rollback.

## Fixed scenario / inputs
- At least five cases must use exact known answers from Northstar; at least five must allow multiple valid tool trajectories.

## Constraints
- Do not use one LLM judge for every metric
- A trajectory mismatch must not fail a case when an alternate valid path satisfies outcome constraints

## Acceptance tests
- [ ] Exactly 25+ cases run from one command
- [ ] Numeric known-answer accuracy >=95% on Northstar cases
- [ ] Every case reports node/trajectory/outcome dimensions
- [ ] Forbidden-action grader is deterministic
- [ ] Baseline results are versioned
- [ ] A candidate change cannot be promoted if a no-regression metric worsens

## Deliverables
- `evals/benchmark.jsonl`
- `evals/graders.py`
- `evals/run_evals.py`
- `evals/baseline-results.json`
- `evals/report.md`
- `PROMOTION_POLICY.md`
- `evals/candidate-results.json`
- `evals/promotion-decision.md`


## Through-project milestone — SQL Harness M10: Frozen Benchmark + Evals

Expand `project/benchmark/` to at least 25 cases across:
- lookup;
- aggregation;
- derived metric;
- comparison;
- diagnostic/multi-step;
- ambiguous;
- unknown schema request;
- unsafe write;
- prompt-injection-like data/context;
- empty-result edge case.

### Required graders
- deterministic SQL safety grader;
- result-equivalence grader (compare canonical result sets, not SQL strings);
- claim-grounding grader;
- route/trajectory assertions for selected cases;
- optional model-based usefulness grader.

### Acceptance
- Benchmark is versioned/frozen before Module 11.
- Runner emits per-case and aggregate JSON.
- Hard safety/correctness cases are separately reported from average score.
- A known deliberate regression causes the suite to fail.
