"""Module 0 baseline placeholder.

Freeze your current 'LLM does everything' implementation here or behind this
interface. Do not improve it after the baseline run; later modules compare
against the frozen version.
"""


def run_baseline(question: str, *, model, schema_text: str) -> dict:
    response = model(question=question, schema=schema_text)
    return {"question": question, "raw_response": response}
