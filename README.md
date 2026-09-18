# Agentic Analytics Engineering — v4.3

A local, project-driven course for turning an **LLM + Skills + the course-supplied Northstar MCP server** into a controlled agentic analytics workflow.

## Free-course guarantee

**Every required lesson, code study, programming assignment, self-grade, and capstone requirement can be completed using free online material.**

The purchased *30 Agents Every AI Engineer Must Build* book is used as an **optional enrichment track**. Precise page ranges remain in the site for readers who own it, but no lab depends on them.

We do lean into Packt material that is genuinely free:

- Packt currently labels **Chapter 2 — The Agent Engineer's Toolkit** a **FREE CHAPTER** on its public site.
- The book's companion GitHub repository is public and supplies the code-archaeology examples used throughout the course.
- Non-free Chapters 4/5/7/8/9 are optional reading; their required concepts are covered by Anthropic, LangGraph, CrewAI, Hugging Face, Phoenix, DeepLearning.AI, and/or the public Packt companion code.

## Run locally

```bash
cd agentic-analytics-engineering
python3 -m http.server 8000
```

Open `http://localhost:8000`.

## What changed in v4.2

- Reclassified every paid Packt chapter as **OPTIONAL**.
- Removed paid-page reading from all required `Source study` assignments.
- Added an explicit **Required/free coverage** block to every module.
- Added Packt **Chapter 2 FREE CHAPTER** to the state/framework module.
- Retained public Packt GitHub code as required code archaeology where it is the strongest example.
- Rewrote `BOOK_MAP.md` / `book-map.html` as a free-first mapping.
- Updated lab assignment files so none require access to the purchased PDF.


## Repository workflow

This repository contains both the course and the cumulative through-project.

```bash
# serve the learning site
./scripts/serve.sh

# run the currently available tests
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
./scripts/test.sh
```

The through-project lives in `project/`; course labs live in `labs/`. GitHub Actions runs the through-project starter tests on every push and pull request.

The lab tests are intentionally red until you complete each assignment. Run them explicitly with `./scripts/test-labs.sh` when working on Modules 1–2.

To create a GitHub remote from a local clone with GitHub CLI:

```bash
./scripts/publish_github.sh agentic-analytics-engineering private
```

Change `private` to `public` only when you intentionally want a public repository.

## Progress data

Progress is stored in browser `localStorage`; use Export/Import to back it up.

## v4.3 — Anthropic cookbooks + course through-project

Two major changes:

1. **Anthropic's public `claude-cookbooks` repository is now a primary free code backbone.** The course explicitly uses the minimal pattern notebooks, current Agent SDK recipes, the Text-to-SQL guide/evaluation suite, session/MCP/safety/hosting recipes, and benchmark examples. See `ANTHROPIC_CODE_MAP.md`.

2. **Every module now advances one through-project:** a self-improving SQL generation agentic harness. The project starts with a frozen “LLM does everything” baseline and ends with a verifier-gated, durable, MCP-capable harness plus a versioned champion/challenger improvement loop. The MCP portion uses only the repository's own Northstar MCP server; no personal or enterprise analytics MCP server is part of the course. See `project.html` and `project/PROJECT_SPEC.md`.

“Self-improving” is deliberately controlled: the production champion never silently edits itself. Failures generate improvement proposals; challengers are evaluated offline; hard safety/correctness gates and approval control promotion; every promoted version is reversible.
