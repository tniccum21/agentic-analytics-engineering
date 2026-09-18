# Free-course note

All Packt code referenced here is from the **public companion GitHub repository**. The purchased PDF is optional enrichment and is not required to perform the code archaeology or labs.

← Course homePackt Code Review: What We Actually Want
Rule: read the code as architecture evidence, not starter code to copy. Each course lab transfers one idea into the self-contained Northstar course context and then proves it with acceptance tests.
Chapter 5 — Planning and task DAGsInspect: PlanningAgent, dependency-aware/topological execution, deadlock/cycle handling, monitoring/revision. Transfer: typed AnalysisPlan + deterministic plan validator/scheduler. Do not copy: demo-specific prompts, provider wrappers, or opaque plan repair.
Chapter 7 — Tool use, manager, workflow/HITLInspect: data_viz_agent Think/Plan/Act + data_state; ManagerAgent specialist delegation; workflow_manager_agent HITL gate; insurance state-machine guards. Transfer: traceable tool loops, structured aggregation, guard conditions. Do not copy: the domain-specific agent chain just because it is multi-agent.
Chapter 8 — Analytics + V&VInspect: Data Analysis stages, Verification & Validation, conflicting evidence, tri_agent_pipeline. Transfer: trust-then-escalate: every candidate finding is VERIFIED, FLAGGED, or ESCALATED before finalization. Keep this separate from the quality critic.
Chapter 9 — failure study + self-improvementInspect: the provider comparison and book's self-improving loop. The repo comparison reports PlannerAgent JSON-parsing failures across cloud providers; our lesson is to enforce structured outputs and fail closed. We reinterpret self-improvement as propose → benchmark → promote/rollback, not autonomous production mutation.
Repo caveat: an open GitHub issue reports that chapter09/README.md shows Chapter 10 material. For Chapter 9, use the purchased PDF plus the actual notebook/comparison artifacts rather than trusting that README.
Source-study artifact expected in labsFor every source-driven lab, SOURCE_NOTES.md should contain: (1) construct inspected, (2) model-vs-code control boundary, (3) one failure mode, (4) what we transfer, and (5) what we deliberately reject.
Official repository · Chapter 9 README issue
