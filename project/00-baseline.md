# Module 0 Through-Project Milestone — Freeze the Baseline Definition

Module 0 is about architecture, not model benchmarking. **Do not run the 12 benchmark cases yet.**

The purpose of this milestone is to preserve a deliberately weak comparison system so later modules can measure what the engineered harness actually improves.

## What the supplied baseline is

The baseline lives in `project/sql_harness/baseline.py`.

Its contract is intentionally minimal:

1. receive one natural-language question;
2. receive the Northstar schema as text;
3. call one model exactly once;
4. return the raw model response.

It has no planner, no tool loop, no SQL verifier, no retry/repair loop, no MCP adapter, no evidence contract, and no claim verifier.

That weakness is intentional. The baseline is the control condition for the course experiment.

## What to do in Module 0

1. Read `project/sql_harness/baseline.py`. Do not improve it.
2. Read all 12 starter cases in `project/benchmark/baseline_cases.jsonl`.
   - Notice that the benchmark includes ordinary analytics questions, an unsafe write request, and an unbounded-extract policy case.
   - Do not delete or rewrite difficult cases.
3. Create the learner baseline record:

   ```bash
   cp project/baseline/BASELINE_TEMPLATE.md project/baseline/BASELINE.md
   ```

4. Fill in `project/baseline/BASELINE.md` with:
   - the baseline purpose;
   - exact inputs and outputs;
   - what the baseline is allowed to do;
   - what safeguards it intentionally does **not** have;
   - the rule that its implementation is frozen after Module 0.
5. Complete `architecture-v0.md` in the Module 0 worksheet by mapping the baseline and proposing the target architecture.
6. Commit the baseline record and architecture artifact.

## What you do **not** do yet

You do **not** need:

- an API key;
- a local model;
- a model provider decision;
- benchmark result files;
- latency/token/cost measurements;
- SQL execution;
- any new safeguards.

Those belong later, after the course has built the execution and evaluation machinery needed to compare systems consistently.

## Why freeze code before running it?

If the baseline keeps changing as the course adds planners, verifiers, adapters, and repair loops, the final comparison becomes meaningless. We freeze the baseline implementation now and execute it later under the same model/configuration used for the engineered harness.

## Acceptance

Module 0 is complete when:

- [ ] `project/sql_harness/baseline.py` remains the supplied one-call baseline.
- [ ] All 12 starter benchmark cases are present and unchanged.
- [ ] `project/baseline/BASELINE.md` documents the baseline contract and missing safeguards.
- [ ] `architecture-v0.md` maps the supplied baseline and proposes a target architecture.
- [ ] No benchmark run has been required in Module 0.
