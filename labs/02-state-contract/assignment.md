# Module 2: Typed State Contract Lab

Turn conversation-like implicit state into an explicit, serializable contract with deterministic merge behavior.

## Tasks
1. Define TaskStatus and WorkflowStatus enums.
2. Implement Pydantic models UserRequest, AnalysisTask, TaskResult, Finding, VisualizationArtifact, Critique, and AnalysisState using the required fields in the starter.
3. Implement merge_task_results(existing, incoming): preserve first-seen task order; replace duplicates by task_id with the newest result; do not duplicate results.
4. Implement state_to_json and state_from_json and prove a round trip reproduces the same semantic state.
5. Add validation: Finding must reference at least one evidence_id; AnalysisTask cannot depend on itself.

## Fixed scenario / inputs
- Use the supplied two-worker merge fixture.
- Do not store the entire application as messages: messages may exist, but the required workflow artifacts must be first-class fields.

## Constraints
- Pydantic v2 or dataclasses + explicit validation
- No LangGraph in this lab
- Reducer behavior must be deterministic

## Acceptance tests
- [ ] Round-trip serialization test passes
- [ ] Duplicate TaskResult replaces rather than appends
- [ ] Parallel merge order is deterministic
- [ ] Finding without evidence is rejected
- [ ] Self-dependent task is rejected

## Deliverables
- `state_models.py`
- `test_state_models.py`
- `state-example.json`

## Through-project milestone — SQL Harness M2: Typed State

Create the durable contract for the SQL harness.

### Required implementation
Add `project/sql_harness/models.py` with typed models for:
- `UserRequest`
- `SchemaContext`
- `SqlCandidate` (`sql`, `attempt`, `generator_version`)
- `VerificationResult` (`status`, `reasons`, `rule_ids`)
- `QueryResult` (`columns`, `rows`, `row_count`, `evidence_id`)
- `Claim` (`text`, `evidence_ids`, `verified`)
- `RunMetrics`
- `HarnessState`
- `ConfigVersion`

### Acceptance
- State round-trips JSON without losing semantic information.
- A settled `Claim` without evidence is rejected.
- A `SqlCandidate` cannot have `attempt < 1`.
- Configuration version is present in every run state.
- Add `project/tests/test_models.py`.
