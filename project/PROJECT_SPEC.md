# Project Specification — SQL Harness

## Goal

Build a model-agnostic, tool-agnostic agentic harness for trustworthy natural-language-to-SQL analytics, then add a controlled offline improvement loop.

## Required properties at capstone

- **Read only by construction:** only SELECT/CTE analytics queries may reach the execution adapter.
- **Typed artifacts:** request, plan, schema context, SQL attempt, verification, execution result, claim, evaluation record, and configuration version are first-class objects.
- **Replaceable hands:** the same harness runs against the bundled Northstar SQLite database either directly or through the **course-supplied Northstar MCP server** by swapping adapters.
- **Self-contained infrastructure:** no user-owned, personal, or enterprise analytics MCP server is required or used anywhere in the course.
- **Bounded autonomy:** model/tool loops have max attempts, budgets, timeouts, and explicit terminal states.
- **Independent verification:** generator output is not trusted merely because the generator says it is correct.
- **Evidence-grounded answers:** settled numeric claims trace to query/result evidence.
- **Durable execution:** runs can be checkpointed/resumed without accidentally re-executing completed work.
- **Regression-driven development:** a frozen benchmark detects quality regressions.
- **Safe improvement:** improvement proposals are evaluated as challengers; no automatic production mutation.
- **Rollback:** champion configuration is versioned and recoverable.

## Interfaces we will converge on

```python
class SchemaProvider(Protocol):
    def get_schema(self, request: str) -> SchemaContext: ...

class SqlExecutor(Protocol):
    def execute_readonly(self, sql: str) -> QueryResult: ...

class SqlGenerator(Protocol):
    def generate(self, state: HarnessState) -> SqlCandidate: ...

class SqlVerifier(Protocol):
    def verify(self, candidate: SqlCandidate, state: HarnessState) -> VerificationResult: ...

class RunEvaluator(Protocol):
    def evaluate(self, run: RunArtifact, case: BenchmarkCase) -> EvalRecord: ...
```

Exact models are assignments, not pre-solved here.

## Improvement unit

A challenger may change only declared configuration surfaces, initially:

- generator prompt/version;
- schema-context selection policy;
- few-shot examples;
- verifier thresholds/rules;
- model routing configuration.

Code changes remain normal software changes and require normal tests/review.

## Promotion gate

A challenger can replace the champion only when all are true:

1. no safety/read-only regression;
2. no decrease on hard deterministic correctness cases;
3. aggregate benchmark quality improves by the configured minimum;
4. unsupported-claim rate does not increase;
5. latency/cost remain inside configured ceilings;
6. required human approval is recorded.
