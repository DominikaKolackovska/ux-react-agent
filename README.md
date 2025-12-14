# UX ReAct Agent
**LLM-driven UX analysis with structured reasoning and tools**

---

## Overview

**UX ReAct Agent** is an experimental Python project exploring how **Large Language Models (LLMs)** can be used not just for generating ideas, but for **systematic UX problem solving**.

Instead of relying on free-form AI recommendations, this project applies the **ReAct (Reason + Act)** pattern to UX analysis:
- the LLM reasons about a UX problem,
- invokes deterministic UX tools when needed,
- and synthesizes the results into **actionable, testable UX decisions**.

The goal is to bridge the gap between **UX intuition** and **data-driven product decisions**.

---

## Why this project exists

In real product teams, UX decisions often suffer from:
- subjective opinions
- lack of prioritization
- vague recommendations
- no clear path to experimentation

This project explores an alternative approach:

> *What if an AI assistant could reason like a UX engineer, use tools like an analyst, and output concrete experiment plans instead of opinions?*

---

## What the agent can do

- Diagnose UX problems using structured reasoning
- Score usability issues using heuristic analysis
- Analyze UX copy readability and cognitive load
- Propose concrete UX improvements
- Generate **experiment-ready A/B test plans** with hypotheses and metrics

All decisions are driven by a **tool-augmented reasoning loop**, not by raw text generation alone.

---

## Architecture (high level)

The agent follows a **ReAct loop**:

1. User describes a UX problem
2. LLM reasons about what information is missing
3. LLM calls a specific UX tool (heuristics, readability, experiments)
4. Python executes the tool deterministically
5. Results are returned to the LLM
6. LLM synthesizes a final UX recommendation

This separation makes the system:
- more transparent
- easier to extend
- easier to audit

---

## Example use case

**Input problem**

> Users drop off during checkout because delivery price is hidden  
> and there is no feedback after clicking the CTA.

**Agent output**

- Identified top usability risks (e.g. visibility of system status)
- Flagged CTA copy as vague and cognitively weak
- Suggested concrete UX fixes (progress indicators, clearer microcopy)
- Proposed A/B tests with hypotheses and success metrics

---

## Tech stack

- Python 3
- OpenAI API (tool calling)
- ReAct reasoning pattern
- Modular, extensible architecture

This project intentionally focuses on **decision quality**, not UI.

---

## Project structure

```text
ux-react-agent/
├── app/
│   ├── __init__.py
│   ├── agent.py        # ReAct loop and tool execution
│   ├── tools.py        # UX analysis tools
│   ├── prompts.py     # System prompt
│   └── main.py        # Entry point
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env