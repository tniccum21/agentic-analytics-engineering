"""Module 2 starter: explicit application state."""
from __future__ import annotations
from enum import Enum
from typing import Any
from pydantic import BaseModel, Field, model_validator

class TaskStatus(str, Enum):
    PENDING="pending"; RUNNING="running"; DONE="done"; FAILED="failed"
class WorkflowStatus(str, Enum):
    NEW="new"; RUNNING="running"; NEEDS_INPUT="needs_input"; DONE="done"; FAILED="failed"

class UserRequest(BaseModel):
    text: str

class AnalysisTask(BaseModel):
    id: str
    objective: str
    dependencies: list[str] = Field(default_factory=list)
    status: TaskStatus = TaskStatus.PENDING
    @model_validator(mode="after")
    def no_self_dependency(self):
        # TODO
        return self

class TaskResult(BaseModel):
    task_id: str
    summary: str
    evidence_ids: list[str] = Field(default_factory=list)
    provenance: dict[str, Any] = Field(default_factory=dict)

class Finding(BaseModel):
    claim: str
    evidence_ids: list[str]
    # TODO: reject empty evidence_ids

class VisualizationArtifact(BaseModel):
    title: str
    spec: dict[str, Any]
    evidence_ids: list[str]

class Critique(BaseModel):
    verdict: str
    required_changes: list[str] = Field(default_factory=list)

class AnalysisState(BaseModel):
    request: UserRequest
    tasks: list[AnalysisTask] = Field(default_factory=list)
    results: list[TaskResult] = Field(default_factory=list)
    findings: list[Finding] = Field(default_factory=list)
    visualizations: list[VisualizationArtifact] = Field(default_factory=list)
    critique: Critique | None = None
    status: WorkflowStatus = WorkflowStatus.NEW


def merge_task_results(existing: list[TaskResult], incoming: list[TaskResult]) -> list[TaskResult]:
    raise NotImplementedError

def state_to_json(state: AnalysisState) -> str:
    raise NotImplementedError

def state_from_json(payload: str) -> AnalysisState:
    raise NotImplementedError
