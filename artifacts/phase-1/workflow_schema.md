# Phase 1 – Workflow DSL Schema

## Supported Format (JSON)

{
  "workflow_name": "string",
  "nodes": [
    {
      "name": "string",
      "type": "tool",
      "config": {
        "message": "string"
      }
    }
  ]
}

---

## Fields

workflow_name (string)
- Identifier for workflow
- Currently not persisted

nodes (array)
- Sequential execution list

node.name (string)
- Unique identifier
- Used in state logs

node.type (string)
- Determines Node class
- Currently supports: "tool"

node.config (object)
- Arbitrary configuration passed to node

---

## Validation Rules

- Unsupported node type → raises error
- Missing nodes → executes empty workflow
- Missing config → defaults to empty dict

---

## Future Extensions

Phase 2:
- conditional nodes
- transitions
- next pointers

Phase 5:
- governance config
- max_steps
- cost limits