# Through-Project: Self-Improving SQL Generation Agentic Harness

This is the course-long project. Every module adds one production-oriented capability to the same system rather than producing disconnected toy agents.

## The product we are building

Given a natural-language analytics request, the harness should:

1. understand the request and decide whether it is simple or requires a multi-step plan;
2. discover only the schema/context it needs;
3. generate one or more SQL candidates;
4. verify the SQL **before execution**;
5. execute through a replaceable read-only capability adapter (direct Northstar SQLite first, then the course-supplied Northstar MCP server);
6. verify returned results and numeric claims;
7. repair/retry within explicit budgets;
8. return an evidence-grounded answer and execution trace;
9. evaluate every run against a benchmark; and
10. propose improvements from failure clusters, test challenger configurations offline, and promote only when deterministic gates pass.

“Self-improving” in this course does **not** mean the production agent silently rewrites itself. Improvement is eval-driven, versioned, reversible, and promotion-gated.

## Final control loop

```text
                     USER QUESTION
                           │
                           ▼
                   REQUEST / ROUTER
                           │
               simple ─────┴───── complex
                 │                    │
                 │                 PLANNER
                 │                    │
                 └──────────┬─────────┘
                            ▼
                      SCHEMA CONTEXT
                            │
                            ▼
                      SQL GENERATOR
                            │
                            ▼
                   PRE-EXEC VERIFIER
                       │          │
                    reject       pass
                       │          │
                     REPAIR       ▼
                       ▲       SQL ADAPTER
                       │          │
                       └──────┐   ▼
                              RESULT CHECKS
                                  │
                                  ▼
                           ANSWER / EVIDENCE
                                  │
                                  ▼
                           RUN EVALUATORS
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                  pass                      failures
                    │                           │
                    ▼                           ▼
              champion stays            FAILURE ANALYZER
                                                │
                                                ▼
                                       IMPROVEMENT PROPOSAL
                                                │
                                      HUMAN / POLICY APPROVAL
                                                │
                                                ▼
                                       CHALLENGER EVALUATION
                                                │
                              promote only if gates all pass
```

## Start here

Read `PROJECT_SPEC.md`, then use `MILESTONES.md` as the cumulative checklist. The `sql_harness/` package is intentionally skeletal: course assignments fill it in. The MCP exercises use only `northstar_mcp/`, the server supplied in this repository.
