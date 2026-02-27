# Phase 1 – Engineering Decisions

## Why Sequential First?

Building graph orchestration immediately introduces:
- State complexity
- Edge handling
- Cycles
- Failure propagation issues

Sequential engine ensures:
- Deterministic execution
- Stable abstraction
- Testable core

We validate the foundation before scaling complexity.

---

## Why Node Abstraction Early?

Even though only ToolNode exists:

We defined BaseNode to:
- Prevent tight coupling
- Allow polymorphism
- Prepare for LLMNode & AgentNode
- Maintain Open-Closed Principle

---

## Why Dictionary-Based State?

Pros:
- Flexible schema
- Easy mutation
- Extensible metadata
- No strict schema limitations

Future:
- Phase 2 → Typed State Models
- Phase 4 → Persisted State Snapshots

---

## Why FastAPI?

- Async-ready
- Auto OpenAPI docs
- Pydantic validation
- Enterprise standard

---

## Why Separate Core from API?

Control plane must be:
- Framework-agnostic
- Testable independently
- Deployable as service or worker

This separation ensures system modularity.

---

## Technical Debt Identified

- No error isolation per node
- No logging per node yet
- No execution trace object
- No versioning

These will be solved in future phases.