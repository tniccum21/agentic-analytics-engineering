"""Frozen Module 0 comparison baseline.

This deliberately weak implementation represents the course's starting point:
one question + schema, one model call, one raw response.

Do not add planners, tools, retries, verifiers, repair loops, MCP, or other
safeguards here. The implementation is frozen in Module 0 and executed later
when the course has built a consistent evaluation runner.
"""


def run_baseline(question: str, *, model, schema_text: str) -> dict:
    response = model(question=question, schema=schema_text)
    return {"question": question, "raw_response": response}
