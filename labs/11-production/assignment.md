# Module 11: Production Chaos Matrix

Prove the agentic workflow fails boundedly, observably, and safely under ten concrete production failure modes.

## Source study / code archaeology
1. FREE source study: review Anthropic trustworthy/reliability guidance plus public Chapter 9 safeguard code. Extract scaling/security/validation/versioning/rollback controls. Optional book deep dive: Ch. 4 pp. 93–115 and Ch. 9 pp. 275–277.
2. Convert each relevant safeguard into an executable chaos case or release gate; prose-only security requirements do not count.
3. Inspect the open Chapter 9 README issue in the repo and note it in your source-quality log: documentation itself is an external dependency that can be stale or wrong.

## Tasks
1. Test these cases: MCP timeout; malformed tool JSON; unavailable capability; prompt injection embedded in metadata; oversized query result; duplicate retry/idempotency; one parallel worker failure; contradictory critic verdicts; budget exhaustion; corrupt/unreadable checkpoint.
2. For each case define expected terminal state, user-visible behavior, retry/escalation behavior, and required trace fields.
3. Run the chaos matrix automatically and generate a report.
4. Release/rollback exercise: version the prompt + Skill + config bundle, inject one change that passes functional tests but fails an eval gate, and prove rollback restores the prior bundle.

## Fixed scenario / inputs
- No case may result in an unbounded loop or silent successful answer based on missing evidence.

## Constraints
- Faults are injected deterministically
- Sensitive/internal stack traces are not surfaced as final user answers
- External data cannot modify system/control policy

## Acceptance tests
- [ ] All 10 chaos cases execute without uncontrolled process failure
- [ ] Every case ends in an allowed terminal state
- [ ] Prompt-injection fixture cannot enable a forbidden tool/action
- [ ] Budget case stops at configured limit
- [ ] Report includes trace/correlation ID for every failure
- [ ] Failed release gate restores the exact prior prompt/Skill/config version

## Deliverables
- `chaos/chaos_cases.yaml`
- `chaos/run_chaos.py`
- `chaos/results.json`
- `production-readiness.md`
- `source-quality-log.md`
- `release-rollback-trace.json`

## Required Anthropic cookbook study

- `claude_agent_sdk/03_The_site_reliability_agent.ipynb`: revisit safety hooks and post-action verification.
- `claude_agent_sdk/07_Hosting_the_agent.ipynb`: compare Docker, managed serverless, and Kubernetes tiers while noting which agent interface remains stable.
- Optional: inspect `scheduled_repository_reviewer/` for bounded unattended runs, `max_turns`, `max_budget_usd`, resumable sessions, and schema-validated continuity.

## Through-project milestone — SQL Harness M11: Safe Self-Improvement

Create `project/sql_harness/improvement.py`.

### Improvement loop
`runs → failure clustering → proposal → approval → challenger config → benchmark → promotion/reject → audit log`

The planner may propose changes only to declared configuration surfaces:
- generator prompt/examples;
- schema-context policy;
- verifier thresholds/rules (within allowed bounds);
- model routing.

### Required version objects
Each `ConfigVersion` records:
- parent version;
- exact diff;
- evidence/failure cluster that motivated it;
- benchmark results;
- approval record;
- promotion/rejection reason.

### Promotion rules
A challenger is rejected if **any** of these occur:
- safety case regression;
- hard deterministic correctness regression;
- unsupported-claim increase beyond tolerance;
- cost/latency ceiling violation.

### Acceptance
- Production/champion config never edits itself in place.
- One deliberately bad prompt change is proposed, benchmarked, and rejected.
- One benign improvement can be promoted only if all gates pass.
- Rollback restores the previous champion exactly.
