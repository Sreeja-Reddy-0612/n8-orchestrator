
Paste:

```md
# Phase 3 – Design Decisions

## 1. Executor Instantiated Per Request

Executor is created inside API route.

Reason:
- Stateless architecture
- No shared global execution state
- Thread-safe
- Production safe

---

## 2. Parser Separated From Executor

WorkflowParser isolates transformation logic.

Reason:
- Clean separation of concerns
- Easier future schema evolution
- Independent unit testing

---

## 3. Node Type Map

NODE_TYPE_MAP used instead of if-else chain.

Reason:
- Extensible
- New node types plug-in easily
- Cleaner architecture

---

## 4. State Dictionary Pattern

Execution state passed between nodes.

Reason:
- Flexible
- Supports tool outputs
- Supports LLM outputs
- Supports conditional routing
- Enables future persistence

---

## 5. Trace Logging

Each node execution appends to trace.

Reason:
- Observability
- Debugging
- Replay in Phase 4
- Governance auditing

---

## 6. MAX_STEPS Guard

Hard limit of 50 execution steps.

Reason:
- Infinite loop protection
- Safety in production
- Prevent runaway workflows