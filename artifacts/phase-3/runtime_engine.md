# Phase 3 – Runtime Engine (Execution Core)

## Objective

Implement the core runtime engine capable of:

- Parsing workflow definitions
- Dynamically resolving nodes
- Executing nodes sequentially
- Handling tool execution
- Maintaining execution state
- Producing structured trace logs

---

## Execution Flow

API → WorkflowExecutor → WorkflowParser → Node → ToolRegistry → Builtin Tool

---

## Components Added

### 1. WorkflowExecutor
Location: core/workflow_engine/executor.py

Responsibilities:
- Accept workflow definition
- Parse nodes
- Execute nodes sequentially
- Maintain state
- Track execution trace
- Prevent infinite loops (MAX_STEPS guard)

---

### 2. WorkflowParser
Location: core/workflow_engine/parser.py

Responsibilities:
- Convert node list into dictionary
- Enable O(1) node lookup by name

---

### 3. ToolNode Execution

ToolNode:
- Fetch tool from ToolRegistry
- Execute tool with provided args
- Append result to state.messages
- Append trace entry
- Store result in state

---

### 4. ToolRegistry

Location: core/tools/registry.py

- Central registry of all tools
- Supports dynamic registration
- Builtins auto-registered on startup

---

## Execution State Structure

Example:

```json
{
  "status": "success",
  "result": {
    "messages": [
      {
        "node": "math_tool",
        "message": "Result: 12"
      }
    ],
    "trace": [
      {
        "node": "tool1",
        "type": "tool",
        "tool_invoked": "math_add"
      }
    ],
    "math_result": 12
  }
}