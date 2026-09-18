import pytest
from state_models import *

def test_round_trip():
    s=AnalysisState(request=UserRequest(text="Why did margin fall?"),findings=[Finding(claim="West GP declined",evidence_ids=["sql:1"])])
    assert state_from_json(state_to_json(s)).model_dump() == s.model_dump()

def test_duplicate_result_replaces_without_reordering():
    a=TaskResult(task_id="a",summary="old")
    b=TaskResult(task_id="b",summary="b")
    anew=TaskResult(task_id="a",summary="new")
    out=merge_task_results([a,b],[anew])
    assert [x.task_id for x in out] == ["a","b"]
    assert out[0].summary == "new"

def test_empty_evidence_rejected():
    with pytest.raises(Exception): Finding(claim="unsupported",evidence_ids=[])

def test_self_dependency_rejected():
    with pytest.raises(Exception): AnalysisTask(id="a",objective="x",dependencies=["a"])
