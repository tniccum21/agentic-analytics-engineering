# Module 12: Capstone Baseline-vs-Agentic System Study

Demonstrate with evidence that the engineered workflow improves reliability/quality enough to justify its added complexity.

## Tasks
1. Freeze the original ‘LLM does everything’ baseline and the final engineered workflow.
2. Run both against the same 25-case evaluation suite with identical model access and data.
3. Compare correctness, unsupported-claim rate, verifier failures caught, tool-call count, latency, token/cost, and convergence iterations.
4. Select three representative traces: straightforward success, revision required, and graceful failure.
5. Present the final architecture and list what you deliberately chose NOT to agentify.

## Fixed scenario / inputs
- No cherry-picking cases. Report all benchmark cases.

## Constraints
- Final recommendation must acknowledge complexity/latency costs
- Architecture diagrams must distinguish control plane, harness, tools/MCP, Skills/context, state/session, critics, and verifiers

## Acceptance tests
- [ ] Both systems run on identical benchmark
- [ ] Final system meets Module 10 thresholds
- [ ] Unsupported-claim rate does not regress
- [ ] At least one reliability metric improves materially
- [ ] All known failures/limitations are documented
- [ ] ADR log reflects final architecture decisions

## Deliverables
- `capstone/CAPSTONE.md`
- `capstone/baseline-results.json`
- `capstone/final-results.json`
- `capstone/traces/`
- `capstone/architecture-final.md`

## Required Anthropic cookbook study

- Revisit `claude_agent_sdk/08_Dynamic_workflows.ipynb`: audit every autonomous region in the final harness and justify why it should be autonomous rather than a deterministic script.
- Revisit `capabilities/text_to_sql/`: compare our final benchmark/evaluation and improvement design to Anthropic's free reference structure.

## Through-project milestone — SQL Harness M12: Capstone + Improvement Study

The capstone is now the finished SQL harness, not a separate project.

### Study A — baseline vs final
Run the frozen Module 0 baseline and final harness on the same benchmark.

### Study B — one full improvement cycle
1. choose a real failure cluster;
2. generate an improvement proposal;
3. approve it for experiment;
4. build challenger config;
5. run full benchmark;
6. promote or reject using Module 11 rules.

### Required report
Include:
- architecture;
- benchmark results;
- three representative traces;
- safety/reliability outcomes;
- latency/cost tradeoff;
- champion/challenger history;
- rollback demonstration;
- “what we deliberately did not agentify.”

### Acceptance
The final project must demonstrate trustworthy improvement through evaluation and promotion gates, not merely a more elaborate agent loop.
