# Module 7: End-to-End Analytics Vertical Slice

Assemble the learned patterns into one complete evidence-grounded analytics workflow, first on the bundled dataset and then through your MCP adapter.

## Source study / code archaeology
1. FREE source study: work through the Phoenix talk-to-data example and inspect `tri_agent_pipeline` in the public Chapter 8 simulation notebook. Identify the explicit boundary between candidate insight generation and verification. Optional book deep dive: Ch. 8 pp. 204–232.
2. Write PIPELINE_MAPPING.md mapping Data Analysis → V&V → GPS from the book onto our Planner/Workers → Verifiers/Critics → reanalysis/escalation architecture.
3. Do not import the book pipeline verbatim; preserve our typed state, evidence IDs, MCP adapter boundary, and deterministic convergence rules.

## Tasks
1. Answer exactly: ‘Why did gross margin fall from Q1 to Q2, and which region contributed most?’
2. Planner creates structured tasks; workers retrieve data; analysis emits Findings with evidence IDs; chart generator emits one visualization spec; verifier recomputes key numeric claims; critics review narrative and chart; finalizer consumes approved artifacts only.
3. Run Part A against Northstar Retail.
4. Run Part B by swapping only the capability adapter to your real MCP-backed source and choose one analogous known-answer question from that system.
5. Implement trust-then-escalate semantics: every Finding ends VERIFIED, FLAGGED, or ESCALATED; finalizer rejects unverified Findings unless explicitly reported as unresolved.

## Fixed scenario / inputs
- Northstar truth: Q1 margin 41.8%; Q2 margin ≈35.98%; change ≈-5.82 percentage points; West gross profit changes 178→148 (-30), the largest negative contribution.

## Constraints
- No raw tool transcript in finalizer context unless explicitly needed
- Every final numeric claim must reference evidence
- Part B may change configuration/mapping but not workflow architecture

## Acceptance tests
- [ ] Northstar answer states the correct margin change within 0.05 pp
- [ ] West is correctly identified as largest negative GP contributor
- [ ] At least one chart passes visualization critic
- [ ] Verifier passes every numeric claim in final answer
- [ ] MCP-backed run completes with same graph/control flow
- [ ] No unverified numeric finding appears as a settled fact in the final report

## Deliverables
- `vertical_slice/`
- `northstar_run.json`
- `mcp_run.json`
- `final_report.md`
- `one chart artifact/spec`
- `PIPELINE_MAPPING.md`
- `SOURCE_NOTES.md`

## Required Anthropic cookbook study

- `capabilities/text_to_sql/guide.ipynb`: trace the full text-to-SQL flow, including schema/context handling and any iterative/self-improvement behavior.
- Write `ANTHROPIC_SQL_NOTES.md` with three ideas we will reuse and three places our typed/verifier-gated harness intentionally differs.

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

Run it twice:
1. bundled Northstar SQLite;
2. real MCP-backed data source using an analogous known-answer question.

### Acceptance
- Northstar margin change is about -5.82 percentage points.
- West is the largest negative gross-profit contributor (-30 dataset units).
- No unverified numeric claim is stated as settled fact.
- Same control graph runs with SQLite and MCP adapters.
