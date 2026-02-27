# Phase 1 – Core Workflow Engine Architecture

## Objective

Build a deterministic sequential workflow executor that:
- Parses workflow definition
- Instantiates node objects
- Executes nodes sequentially
- Passes state between nodes
- Returns structured execution output

No orchestration graph.
No persistence.
No governance.
Pure execution foundation.

---

## High-Level Flow

Client → FastAPI → WorkflowExecutor → Node Execution → State Mutation → JSON Response

---

## Execution Flow

1. User sends workflow JSON via POST /workflow/execute
2. FastAPI receives request
3. WorkflowExecutor initialized
4. Executor builds node objects
5. StateManager initializes state
6. Nodes execute sequentially
7. Each node mutates state
8. Final state returned

---

## Core Components

### 1. WorkflowExecutor
Responsible for:
- Parsing node definitions
- Instantiating correct node class
- Sequential execution
- State passing

---

### 2. BaseNode (Abstraction)

Defines contract:

execute(state: Dict) -> Dict

Ensures future extensibility:
- LLMNode
- ToolNode
- AgentNode
- ConditionNode

---

### 3. ToolNode (Phase 1 Implementation)

Simple deterministic node:
- Reads config.message
- Appends structured output to state

---

### 4. StateManager

Initializes workflow state:

{
    "messages": [],
    "metadata": {}
}

State is mutable and passed forward.

---

## Architectural Decisions

- Sequential execution first (avoid premature complexity)
- State stored as dictionary for flexibility
- Node abstraction from day one
- Executor separated from API layer
- Observability module reserved for structured logging

---

## What This Enables

Phase 2:
- Graph-based routing
- Conditional branching
- Loop support

Phase 3:
- Tool registry
- LLM integration
- Agent execution

This is the control-plane foundation.