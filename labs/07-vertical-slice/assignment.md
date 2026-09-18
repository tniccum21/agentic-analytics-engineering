# Module 7: End-to-End Analytics Vertical Slice

Assemble the learned patterns into one complete evidence-grounded analytics workflow, first through the direct SQLite adapter and then through the course-supplied Northstar MCP server.

## Study evidence

Complete the module's single **Study Plan** in the course site first. This section is not an additional reading list; it specifies the observations and artifacts to capture from those sources.
1. FREE source study: work through the Phoenix talk-to-data example and inspect `tri_agent_pipeline` in the public Chapter 8 simulation notebook. Identify the explicit boundary between candidate insight generation and verification. Optional book deep dive: Ch. 8 pp. 204–232.
2. Write PIPELINE_MAPPING.md mapping Data Analysis → V&V → GPS from the book onto the course Planner/Workers → Verifiers/Critics → reanalysis/escalation architecture.
3. Do not import the book pipeline verbatim; preserve the course's typed state, evidence IDs, MCP adapter boundary, and deterministic convergence rules.


### Additional code-study prompts

- `capabilities/text_to_sql/guide.ipynb`: trace the full text-to-SQL flow, including schema/context handling and any iterative/self-improvement behavior.
- Write `ANTHROPIC_SQL_NOTES.md` with three ideas we will reuse and three places the course's typed/verifier-gated harness intentionally differs.

## Tasks
1. Answer exactly: ‘Why did gross margin fall from Q1 to Q2, and which region contributed most?’
2. Planner creates structured tasks; workers retrieve data; analysis emits Findings with evidence IDs; chart generator emits one visualization spec; verifier recomputes key numeric claims; critics review narrative and chart; finalizer consumes approved artifacts only.
3. Run Part A against Northstar Retail through the direct `SQLiteReadOnlyAdapter`.
4. Run Part B against the **same Northstar Retail dataset** through the course-supplied Northstar MCP server by swapping only the capability adapter.
5. Implement trust-then-escalate semantics: every Finding ends VERIFIED, FLAGGED, or ESCALATED; finalizer rejects unverified Findings unless explicitly reported as unresolved.

## Fixed scenario / inputs
- Northstar truth: Q1 margin 41.8%; Q2 margin ≈35.98%; change ≈-5.82 percentage points; West gross profit changes 178→148 (-30), the largest negative contribution.
- Part A and Part B must answer the same known-answer question against the same underlying Northstar data.

## Constraints
- No raw tool transcript in finalizer context unless explicitly needed
- Every final numeric claim must reference evidence
- Part B may change the capability adapter only; workflow architecture, question, and expected answer remain unchanged
- No external or user-owned analytics MCP server is used anywhere in this course

## Acceptance tests
- [ ] Northstar answer states the correct margin change within 0.05 pp
- [ ] West is correctly identified as largest negative GP contributor
- [ ] At least one chart passes visualization critic
- [ ] Verifier passes every numeric claim in final answer
- [ ] Northstar MCP-backed run completes with the same graph/control flow
- [ ] Direct-SQLite and Northstar-MCP runs produce equivalent settled numeric results
- [ ] No unverified numeric finding appears as a settled fact in the final report

## Deliverables
- `vertical_slice/`
- `northstar_sqlite_run.json`
- `northstar_mcp_run.json`
- `final_report.md`
- `one chart artifact/spec`
- `PIPELINE_MAPPING.md`
- `SOURCE_NOTES.md`


## Through-project milestone — SQL Harness M7: Complete Vertical Slice

Run the harness end to end.

### Required run
Question: **“Why did gross margin fall from Q1 to Q2, and which region contributed most?”**

Produce:
- structured plan;
- schema context;
- all SQL attempts;
- verification records;
- query results/evidence IDs;
- final claims;
- final answer;
- one visualization spec;
- full trace.

Run it twice against the same bundled Northstar data:
1. direct `SQLiteReadOnlyAdapter`;
2. `McpSqlAdapter` → course Northstar MCP server.

### Acceptance
- Northstar margin change is about -5.82 percentage points.
- West is the largest negative gross-profit contributor (-30 dataset units).
- No unverified numeric claim is stated as settled fact.
- Same control graph runs with direct SQLite and Northstar MCP adapters.
- Both runs settle on equivalent numeric results.
