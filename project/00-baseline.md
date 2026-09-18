# Module 0 Through-Project Milestone — Freeze the SQL Baseline

Before improving anything, capture the **course-supplied minimal baseline** that intentionally represents an “LLM does everything” approach. No pre-existing learner analytics system is assumed.

## Assignment

1. Use the supplied baseline runner in `project/sql_harness/baseline.py`, choose one model/configuration, and freeze it for baseline comparison.
2. Give it the Northstar schema and the 12 starter benchmark questions in `benchmark/baseline_cases.jsonl`.
3. Record for every case:
   - raw response;
   - SQL proposed, if any;
   - whether SQL was executed;
   - returned result;
   - final answer;
   - latency;
   - token/cost data if available;
   - any unsupported claim or unsafe action.
4. Do **not** add repair loops, planners, verifiers, or retries yet.
5. Write `baseline/BASELINE.md` describing exactly what the baseline is allowed to do.

## Acceptance

- All 12 cases are recorded without cherry-picking.
- Unsafe/write requests are included, even if the baseline handles them badly.
- Model name/configuration and prompt are versioned.
- Baseline artifacts are frozen after Module 0 except for bug fixes required to reproduce the original behavior.
- `architecture-v0.md` shows the **supplied course baseline** and target harness side by side.
