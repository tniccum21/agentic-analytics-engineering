"""Module 1 starter. Implement without agent frameworks."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable

@dataclass
class TraceEvent:
    kind: str
    payload: dict[str, Any]

@dataclass
class RunResult:
    output: Any
    trace: list[TraceEvent] = field(default_factory=list)
    stop_reason: str = "completed"


def single_shot_route(request: str, model: Any) -> RunResult:
    """Exactly one model call; zero tools. Return structured route decision."""
    raise NotImplementedError


def react_agent(goal: str, model: Any, tools: dict[str, Callable], max_steps: int = 4) -> RunResult:
    """Loop over model actions and tool observations, capped by max_steps."""
    raise NotImplementedError


def planner_executor(goal: str, planner: Any, executors: dict[str, Callable]) -> RunResult:
    """Planner emits tasks with id/dependencies/executor/input; code executes when ready."""
    raise NotImplementedError


def reflexive_agent(request: str, generator: Any, critic: Any, max_revisions: int = 2) -> RunResult:
    """Generate, critique, revise. Critic returns verdict/issues/required_changes."""
    raise NotImplementedError


def verifier_gated(proposal: dict, verifier: Callable, tools: dict[str, Callable]) -> RunResult:
    """Verification MUST occur before any proposed tool executes."""
    raise NotImplementedError
