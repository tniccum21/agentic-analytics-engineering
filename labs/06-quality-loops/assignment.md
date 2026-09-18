# Module 6: Critic, Verifier, and Revision Lab

Demonstrate that quality critique and correctness verification are different mechanisms with different authority.

## Study evidence

Complete the module's single **Study Plan** in the course site first. This section is not an additional reading list; it specifies the observations and artifacts to capture from those sources.
1. FREE source study: study Anthropic evaluator-optimizer and inspect Verification & Validation / `tri_agent_pipeline` in the public Chapter 8 simulation notebook. Optional book deep dive: Ch. 8 pp. 211–215 and 231–232.
2. Diagram trust-then-escalate: candidate finding → verification → verified OR flagged → resolver/escalation. Contrast it with generate → critic → revise.
3. FREE source study: inspect public `chapter09/self_improving.py` and note why an improvement proposal is not itself evidence that the system improved. Optional book deep dive: Ch. 9 pp. 265–277.


### Additional code-study prompts

- `patterns/agents/evaluator_optimizer.ipynb`: identify the evaluator output, revision input, and exit condition.
- `claude_agent_sdk/08_Dynamic_workflows.ipynb`: inspect fan-out verification and skeptic/adversarial checking. Explain why an independent verifier is not the same thing as a reflective critic.

## Tasks
1. Implement AnalysisCritic producing rubric scores for evidence support, alternative explanations, causal language, completeness, and executive usefulness.
2. Implement VisualizationCritic producing rubric scores for chart choice, labeling, scale, clutter, and question relevance.
3. Implement deterministic NumericVerifier that recomputes any claimed margin delta from source values.
4. Run generate → verify → critique → revise with max_revisions=2.
5. Create a case where critic quality is high but NumericVerifier fails, proving verification gates correctness independently.
6. Fixture C: two evidence sources disagree on the same metric; verifier returns CONFLICT and routes to escalation/reanalysis.
7. Fixture D: numeric claim is correct but evidence_id is missing; grounding verifier blocks finalization even though NumericVerifier passes.

## Fixed scenario / inputs
- Fixture A claims margin fell 4.2 points; bundled data truth is about 5.82 points.
- Fixture B chart truncates a bar-axis in a way that exaggerates a small difference.

## Constraints
- Verifier cannot call the same generator prompt/model path as its sole evidence
- Verifier failure blocks acceptance
- Critic feedback alone does not override a verifier failure

## Acceptance tests
- [ ] Wrong 4.2-point claim is rejected
- [ ] Correct recomputed delta passes
- [ ] Bad chart receives revise verdict
- [ ] Revision loop cannot exceed two revisions
- [ ] Trace distinguishes verifier events from critic events
- [ ] Conflicting-evidence fixture escalates instead of auto-resolving
- [ ] Correct-but-ungrounded claim is blocked

## Deliverables
- `critics.py`
- `verifiers.py`
- `revision_loop.py`
- `fixtures/`
- `test_quality_loop.py`
- `SOURCE_NOTES.md`


## Through-project milestone — SQL Harness M6: Verification and Repair

Create `project/sql_harness/verification.py` with three distinct gates.

### Gate A — pre-execution SQL verifier
Deterministically reject:
- non-read-only statements;
- multiple statements;
- unknown tables/columns from supplied schema;
- queries violating configured row-limit policy.

### Gate B — result verifier
Check:
- expected result shape;
- non-empty/empty semantics;
- arithmetic recomputation for known derived metrics;
- required comparison groups are present.

### Gate C — claim verifier
Every final numeric claim must point to evidence and recompute/compare within tolerance.

### Repair loop
A failed SQL candidate may be repaired at most 2 times. The generator receives structured verifier reasons, not a generic “try again.”

### Acceptance
- Critic feedback cannot override a hard verifier rejection.
- Known bad SQL fixtures never execute.
- The Q1/Q2 gross-margin answer recomputes within 0.05 percentage points.
- Repair trace shows failure reason → changed SQL → pass/final fail.
