# Phase 2 – Workflow DSL Extension

## New Required Field

start_at: string

Defines the entry node of workflow.

---

## Node Routing Fields

For tool nodes:

"next": "node_name" | null

For condition nodes:

"on_true": "node_name"
"on_false": "node_name"

---

## Condition Node Config

{
  "condition_key": "string",
  "equals": "value"
}

Behavior:
If state[condition_key] == equals:
    go to on_true
Else:
    go to on_false

---

## Safety

If start_at missing:
Exception raised.

If next node missing:
Exception raised.

If max steps exceeded:
Execution halted.