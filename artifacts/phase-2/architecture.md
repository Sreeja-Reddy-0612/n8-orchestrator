# Phase 2 – Graph-Based Workflow Orchestration Engine

## Objective

Upgrade the execution engine from sequential execution to
graph-based dynamic orchestration.

This phase introduces:

- Directed graph traversal
- Conditional routing
- Execution pointer management
- Step guard for infinite loop protection
- Structured execution trace

This transforms the system from a pipeline runner into an orchestrator core.

---

## Architectural Upgrade

Phase 1:
Sequential execution (for loop)

Phase 2:
While-loop execution with dynamic node pointer.

Execution model now:

current_node → execute → determine next → move pointer → repeat

---

## Execution Flow

1. Read workflow.start_at
2. Initialize state
3. Initialize StepGuard
4. While current_node exists:
   - Increment guard
   - Execute node
   - Append execution trace
   - Resolve next node
5. Return final state

---

## New Components

### 1. ConditionNode

Evaluates condition using:

- condition_key
- equals

Sets internal _condition_result flag.

Routing handled by executor.

---

### 2. StepGuard

Purpose:
Prevent infinite loops.

Default:
max_steps = 25

If exceeded:
Raise exception.

This is critical for production AI systems.

---

### 3. Execution Pointer

Instead of iterating list,
we now track:

current_node_name

This enables:

- Dynamic routing
- Branching
- Future loop support

---

## Supported DSL (Phase 2)

{
  "workflow_name": "...",
  "start_at": "node_name",
  "nodes": [
    {
      "name": "node",
      "type": "tool" | "condition",
      "config": {},
      "next": "node_name",
      "on_true": "node_name",
      "on_false": "node_name"
    }
  ]
}

---

## Execution Trace Structure

State now includes:

"trace": [
    {
        "node": "step1",
        "type": "tool"
    },
    {
        "node": "decision",
        "type": "condition",
        "evaluated_key": "route",
        "value": null
    }
]

This enables:

- Observability
- Debugging
- Replay preparation (Phase 4)