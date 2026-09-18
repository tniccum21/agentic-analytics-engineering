# 30 Agents — Free-First Reading & Code Map

## Course policy

**The course remains fully completable for free.** No purchased chapter is a prerequisite for a lesson, lab, self-grade, or capstone requirement.

We use *30 Agents Every AI Engineer Must Build* in three ways:

1. **Free Packt material** — especially the public GitHub companion code and Packt's online free chapter(s) — may be required.
2. **Other free sources** — Anthropic, LangGraph, CrewAI, Hugging Face, Phoenix, DeepLearning.AI, etc. — provide complete coverage of every required concept.
3. **Paid book chapters** — precise page ranges are optional enrichment for students who own the book.

Packt currently labels **Chapter 2, “The Agent Engineer's Toolkit,” as a FREE CHAPTER** on its public book pages. The companion GitHub repository for the implementation chapters is also public.

| Module | Required free coverage | Optional paid Packt reading |
|---|---|---|
| 0 — Architecture | Anthropic Managed Agents, context engineering, Building Effective Agents | Ch. 1 pp. 4–19 |
| 1 — Core patterns | DeepLearning.AI agent-from-scratch + public Packt Ch. 5/7 notebooks | Ch. 5 pp. 118–135; Ch. 7 pp. 174–186 |
| 2 — State | LangChain Academy/LangGraph docs + **Packt Ch. 2 free chapter** | Ch. 5 pp. 135–144 |
| 3 — Routing/orchestration | LangGraph patterns + Anthropic orchestrator-workers + public Packt Ch. 7 code | Ch. 7 pp. 186–200 |
| 4 — MCP boundary | Hugging Face MCP course + public Packt Ch. 7 tool code | Ch. 1 pp. 15–19; Ch. 7 pp. 174–185 |
| 5 — Planning | Anthropic orchestrator-workers + public Packt Ch. 5 planning code + Ch. 9 public failure study | Ch. 5 pp. 131–137 |
| 6 — Critic/verifier | Anthropic evaluator-optimizer + Andrew Ng reflection + public Packt Ch. 8/9 code | Ch. 8 pp. 211–215, 231–232; Ch. 9 pp. 265–277 selective |
| 7 — Analytics | Phoenix talk-to-data + public Packt Ch. 8 implementation | Ch. 8 pp. 204–232 |
| 8 — Durability/HITL | LangGraph persistence/HITL + public Packt Ch. 7 workflows | Ch. 7 pp. 195–200 |
| 9 — Multi-agent | CrewAI docs/course + public Packt Ch. 7 manager code | Ch. 7 pp. 186–195 |
| 10 — Evals | DeepLearning.AI evals + Anthropic eval guidance + public Packt Ch. 9 code | Ch. 9 pp. 265–277 |
| 11 — Production | Anthropic trustworthy/reliability material + public Packt Ch. 9 safeguard code | Ch. 4 pp. 93–115; Ch. 9 pp. 275–277 |
| 12 — Capstone | All free course sources + your SOURCE_NOTES and eval evidence | Optional selective reread of Ch. 5/7/8/9 |

## Required Packt code is free

The public companion repository is the code source for the course. Prefer the `__RUN_NO_KEY_SIMULATION.ipynb` files for stable walkthroughs:

- `chapter05/ch05_foundational_architectures__RUN_NO_KEY_SIMULATION.ipynb`
- `chapter07/ch07_tool_orchestration__RUN_NO_KEY_SIMULATION.ipynb`
- `chapter08/ch08_data_analysis_reasoning_agents__RUN_NO_KEY_SIMULATION.ipynb`
- `chapter09/LLM_COMPARISON.md`
- `chapter09/self_improving.py`
- `chapter09/state_models.py`

## Transfer rule

Do not copy a demo architecture wholesale. For each source, record:

1. construct inspected;
2. model-vs-code control boundary;
3. one failure mode;
4. what we transfer into the **Northstar course exercise**; and
5. what we deliberately reject.
