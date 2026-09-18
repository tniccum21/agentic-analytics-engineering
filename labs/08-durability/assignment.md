# Module 8: Durability + Failure Injection Lab

Make the workflow resumable and prove failure semantics with deterministic injected faults.

## Study evidence

Complete the module's single **Study Plan** in the course site first. This section is not an additional reading list; it specifies the observations and artifacts to capture from those sources.
1. FREE source study: review LangGraph persistence/HITL and inspect `workflow_manager_agent` plus the insurance workflow/state-machine section in the public Chapter 7 notebook. Optional book deep dive: Ch. 7 pp. 195–200.
2. List every guard condition you can find and classify it as retry, reject, escalate/HITL, or continue. Then implement the supplied analytics-specific guards rather than the e-commerce/insurance rules.
3. Record checkpoint semantics separately from model context: what must survive a process crash, and what can be recomputed.


### Additional code-study prompts

- `claude_agent_sdk/05_Building_a_session_browser.ipynb`: inspect session listing, transcript replay, fork, and resume.
- Map those concepts onto a provider-neutral SQL-harness run/session model; do not couple the project to Claude-specific transcript storage.

## Tasks
1. Fault 1: data tool times out twice, succeeds on third call; retry policy permits exactly 3 attempts.
2. Fault 2: planner marks request ambiguous; graph interrupts and resumes after supplied clarification.
3. Fault 3: simulate process crash after two workers complete; restart from checkpoint and do not repeat completed idempotent workers.
4. Fault 4: critic requests additional evidence; route back to analysis once, then continue to synthesis.
5. Record attempt count and checkpoint ID in trace.
6. Guard fixture: confidence=0.82 must interrupt for HITL; confidence=0.91 may continue automatically. The 0.85 threshold is workflow configuration, never model-selected.

## Fixed scenario / inputs
- Use a deterministic failure injector; do not depend on random failures.

## Constraints
- Retries must distinguish transient CapabilityError from validation failure
- No retry loop can be unbounded
- Checkpoint state must be serializable

## Acceptance tests
- [ ] Timeout case succeeds on exactly attempt 3
- [ ] Ambiguous case pauses before data query
- [ ] Resume case does not duplicate completed worker result
- [ ] Critic-to-analysis back-edge occurs at most once in fixture
- [ ] Exhausted retries end in explicit failed status
- [ ] 0.82 confidence triggers HITL and 0.91 does not

## Deliverables
- `durable_graph.py`
- `failure_injector.py`
- `test_durability.py`
- `resume-trace.json`
- `SOURCE_NOTES.md`


## Through-project milestone — SQL Harness M8: Durable Sessions

Add `project/sql_harness/persistence.py`.

### Required failure drills
1. Crash after SQL verification but before execution; resume without regenerating a different candidate unless policy says to.
2. Crash after successful execution; resume without executing the same SQL again.
3. Ambiguous question interrupts for user clarification; resume with the clarification.
4. Adapter timeout retries twice and then returns a typed terminal failure.

### Acceptance
- Every run has `run_id`, checkpoint sequence, and configuration version.
- Completed execution is idempotent on resume.
- Session history can be inspected without invoking the model.
- Resume test proves no duplicate SQL execution.
