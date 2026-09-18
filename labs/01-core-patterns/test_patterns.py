"""Supplied acceptance tests for Module 1. Run: python -m pytest -q"""
import pytest
from patterns import single_shot_route, react_agent, planner_executor, reflexive_agent, verifier_gated

class QueueModel:
    def __init__(self, replies): self.replies=list(replies); self.calls=0
    def invoke(self, payload):
        self.calls += 1
        if not self.replies: raise AssertionError("Model called too many times")
        return self.replies.pop(0)

def test_single_shot_calls_model_once():
    m=QueueModel([{"route":"analysis","rationale":"requires aggregation"}])
    r=single_shot_route("Why did margin fall?",m)
    assert m.calls == 1
    assert r.output["route"] == "analysis"
    assert len(r.trace) >= 1

def test_react_executes_tools_and_stops():
    m=QueueModel([
        {"type":"tool","tool":"gp_change","input":{"region":"West"}},
        {"type":"final","answer":"West, -30"}
    ])
    calls=[]
    def gp_change(region): calls.append(region); return -30
    r=react_agent("largest decline",m,{"gp_change":gp_change},max_steps=4)
    assert calls == ["West"]
    assert r.output == "West, -30"
    assert r.stop_reason == "completed"

def test_react_hard_stops_at_four_steps():
    m=QueueModel([{"type":"tool","tool":"ping","input":{}} for _ in range(10)])
    n={"calls":0}
    def ping(): n["calls"]+=1; return "pong"
    r=react_agent("never ending",m,{"ping":ping},max_steps=4)
    assert n["calls"] == 4
    assert m.calls == 4
    assert r.stop_reason in {"max_steps","budget_exhausted"}

def test_planner_respects_dependencies():
    plan=[
      {"id":"a","dependencies":[],"executor":"collect","input":"Q1"},
      {"id":"b","dependencies":["a"],"executor":"analyze","input":"margin"}
    ]
    class Planner:
        def invoke(self,goal): return plan
    order=[]
    def collect(x): order.append("a"); return {"q":x}
    def analyze(x): order.append("b"); return {"finding":x}
    r=planner_executor("Explain margin",Planner(),{"collect":collect,"analyze":analyze})
    assert order == ["a","b"]
    assert r.output is not None

def test_reflexive_never_exceeds_two_revisions():
    generated=[]
    def gen(payload): generated.append(payload); return f"draft-{len(generated)}"
    critiques=iter([
       {"verdict":"revise","issues":["unsupported"],"required_changes":["remove claim"]},
       {"verdict":"revise","issues":["wordy"],"required_changes":["shorten"]},
       {"verdict":"revise","issues":["still"],"required_changes":["again"]},
    ])
    def critic(x): return next(critiques)
    r=reflexive_agent("write summary",gen,critic,max_revisions=2)
    assert len(generated) == 3  # initial + 2 revisions
    assert r.stop_reason in {"max_revisions","budget_exhausted"}

def test_verifier_prevents_rejected_tool_call():
    calls=[]
    def execute(sql): calls.append(sql); return "executed"
    def verifier(p): return {"approved":False,"reason":"write query forbidden"}
    r=verifier_gated({"tool":"sql","input":"DELETE FROM sales"},verifier,{"sql":execute})
    assert calls == []
    assert r.stop_reason in {"rejected","verification_failed"}

def test_verifier_allows_approved_tool_call_once():
    calls=[]
    def execute(sql): calls.append(sql); return [{"region":"West"}]
    def verifier(p): return {"approved":True,"reason":"read-only bounded query"}
    r=verifier_gated({"tool":"sql","input":"SELECT region FROM sales LIMIT 10"},verifier,{"sql":execute})
    assert len(calls) == 1
    assert r.output == [{"region":"West"}]
