Phase 8 – Dependency-Based DAG Execution Engine
Objective

Upgrade the workflow execution engine from sequential execution to a dependency-driven DAG scheduler capable of handling:

Multiple root nodes

Branch convergence

Deadlock detection

Deterministic graph scheduling

Architectural Changes
1. Execution Model Upgrade

Previous model:

Linear execution

start_at

next routing

Conditional branching via true_next / false_next

New model:

Dependency-driven execution

depends_on field

Graph scheduling logic

Topological execution resolution

New Workflow Format
{
  "nodes": [
    {
      "name": "add_node",
      "type": "tool",
      "depends_on": [],
      "config": {
        "tool": "math_add",
        "args": { "a": 10, "b": 5 }
      }
    },
    {
      "name": "llm_node",
      "type": "llm",
      "depends_on": ["add_node"],
      "config": {
        "prompt": "Execution complete."
      }
    }
  ]
}
Execution Algorithm

Build node map

Track:

completed

failed

Iterate until all nodes processed:

Execute nodes whose dependencies are completed

Mark progress

If no progress made → Deadlock detected

Return execution result + trace

Key Enhancements
Dependency Validation

Ensures all depends_on references exist

Prevents invalid workflow submission

Deadlock Detection

Detects circular dependencies

Prevents infinite execution loops

Multi-Root Support

Nodes with empty depends_on execute independently

Branch Convergence

Nodes can wait on multiple upstream nodes

Standardized Node Output

All nodes now return structured output:

{
  "node": "node_name",
  "type": "tool | condition | llm",
  "output": { ... }
}
State Structure

State now stores full node result:

state = {
  "add_node": { full node output },
  "multiply_node": { full node output },
  ...
}

This enables consistent downstream access.

Frontend Alignment

Updated dashboard payload to DAG format:

Removed start_at

Removed next

Introduced depends_on

Verified execution history integration remains stable

System Capabilities After Phase 8

✔ Directed Acyclic Graph execution
✔ Multi-root workflows
✔ Dependency validation
✔ Deadlock detection
✔ Retry logic retained
✔ Execution trace logging
✔ Execution persistence
✔ Frontend integration stable

System Maturity Level

MVP DAG Orchestration Engine

Single-process
Graph-aware scheduler
Deterministic execution
In-memory persistence