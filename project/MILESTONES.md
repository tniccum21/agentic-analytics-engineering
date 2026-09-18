# Through-Project Milestones

| Module | Project milestone | Concrete artifact |
|---|---|---|
| 0 | Freeze baseline and architecture | `baseline/`, `architecture-v0.md` |
| 1 | Implement five reusable control-flow primitives | `sql_harness/patterns.py`, traces |
| 2 | Define typed harness state/artifacts | `sql_harness/models.py` |
| 3 | Build explicit SQL harness graph | `sql_harness/graph.py` |
| 4 | Isolate SQLite/MCP capability adapters | `sql_harness/adapters/` |
| 5 | Add structured plan/clarification path | `sql_harness/planner.py` |
| 6 | Add pre-exec verifier + repair + result/claim verification | `sql_harness/verification.py` |
| 7 | Complete NL→SQL→answer vertical slice | `runs/northstar/` + MCP run |
| 8 | Add checkpoints/resume/idempotency | `sql_harness/persistence.py` |
| 9 | Compare one subproblem using CrewAI; retain only evidence-backed value | comparison report |
| 10 | Freeze benchmark and automated eval runner | `benchmark/`, `sql_harness/evals.py` |
| 11 | Add versioned champion/challenger improvement loop | `sql_harness/improvement.py` |
| 12 | Run baseline vs final + improvement-cycle study | capstone report and traces |
