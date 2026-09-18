# Frozen Baseline

This directory holds the learner's description of the deliberately weak comparison system.

In Module 0, copy the supplied template:

```bash
cp project/baseline/BASELINE_TEMPLATE.md project/baseline/BASELINE.md
```

Then fill in the contract. **Do not run the benchmark yet.**

The baseline implementation itself lives in `project/sql_harness/baseline.py` and is frozen after Module 0. Later, once the evaluation runner exists, the course executes that frozen baseline against the benchmark using the same model/configuration as the engineered harness.
