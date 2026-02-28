# Phase 2 – Engineering Decisions

## Why Build Graph Engine Manually Instead of LangGraph?

Reasons:

1. Understand orchestration mechanics
2. Control execution model
3. Avoid hidden abstraction
4. Prepare for custom governance rules
5. Prevent vendor dependency

LangGraph may be integrated later,
but foundation must be native.

---

## Why StepGuard Is Critical?

AI agents can:

- Loop infinitely
- Re-enter decision nodes
- Re-trigger themselves

StepGuard ensures:

- Deterministic safety
- Production readiness
- System stability

This is infrastructure-level thinking.

---

## Why Execution Pointer Instead of Recursion?

While-loop pointer model:

- Easier to reason about
- Prevents stack overflow
- More production-safe
- Easier to checkpoint later

---

## Why Trace Stored in State?

We chose to store trace inside state because:

- Enables replay
- Enables persistence
- Enables version comparison
- Enables debugging

Future phases:
Trace will move to observability layer.

---

## Technical Debt Identified

- Trace currently duplicates decision logging
- No node-level error isolation
- No execution ID
- No version tagging
- No timing metrics

These will be solved in Phase 3–5.