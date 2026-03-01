## N8 Orchestrator
Enterprise AI Workflow Control Plane

Enterprise-grade AI workflow orchestration engine designed to execute, monitor, and audit multi-step AI workflows across tools, LLMs, and conditional logic.

This system provides deterministic DAG execution, async orchestration, observability, and audit-ready persistence for production AI systems.

It is not a chatbot.

It is not an agent wrapper.

It is a structured AI execution control plane.

## Problem Statement

Most AI systems in production fail not because models are weak —
but because workflows are:

Unstructured

Non-deterministic

Unobservable

Unrecoverable

Non-auditable

In real enterprise environments:

Multi-step LLM chains break silently

Tool execution fails without retries

No execution trace exists

No visibility into per-node latency

No failure control policies

No audit trail for compliance

As LLM systems move from demos to business-critical workflows,
lack of orchestration becomes a reliability risk.

##  Solution Overview

N8-Orchestrator is a workflow execution engine that:

Executes Directed Acyclic Graphs (DAGs)

Supports async parallel node execution

Handles tool nodes, LLM nodes, and conditional nodes

Implements retry & timeout policies

Tracks per-node execution status

Records execution traces

Persists workflow results

Exposes REST APIs for integration

Provides a full React dashboard

Enables observability & audit-ready tracking

The system behaves as an AI workflow control plane, not a prompt chain.

##  Core Capabilities
1️⃣ Deterministic DAG Execution

Dependency-based node scheduling

Circular dependency detection

Deadlock prevention

Explicit convergence handling

2️⃣ Async Parallel Execution

asyncio-based concurrency

Parallel node scheduling

Non-blocking execution model

Safe state synchronization via locks

3️⃣ Node Types Supported
Tool Nodes

Custom business logic execution.

Example:

{
  "type": "tool",
  "config": {
    "tool": "math_add",
    "args": { "a": 10, "b": 5 }
  }
}
### LLM Nodes 

Language model execution layer.

### Conditional Nodes

Branching based on runtime state.

4️⃣ Retry & Timeout Policies

Per-node configuration:

"retry": {
  "max_retries": 2,
  "delay_seconds": 1,
  "timeout_seconds": 5
}

## Features:

Controlled retries

Timeout enforcement

Failure state tracking

Graceful degradation

5️⃣ Observability & Traceability

Each execution records:

Execution ID

Overall status

Node-level output

Node-level status

Error logs

Execution trace

Completion tracking

Enables full workflow replay and debugging.

6️⃣ Persistence Layer

SQLite-based execution storage

Execution history tracking

API-accessible audit records

Immutable execution snapshots

7️⃣ React Governance Dashboard

Frontend provides:

Workflow execution trigger

Execution history viewer

Detailed execution trace view

Node-level result cards

Dark-mode enterprise UI

Real-time backend integration

##  System Architecture
```
User / Application
        ↓
React Dashboard (Vite)
        ↓
FastAPI Workflow API
        ↓
Workflow Executor Engine
 ├─ DAG Scheduler
 ├─ Async Execution Manager
 ├─ Retry & Timeout Controller
 ├─ Node Dispatcher
 │    ├─ Tool Node
 │    ├─ LLM Node
 │    └─ Condition Node
        ↓
State & Trace Manager
        ↓
Persistence Layer (SQLite)
        ↓
Execution History & Audit APIs
```
##  Core APIs
Execute Workflow
POST /workflow/execute

Request body:

{
  "nodes": [ ... ]
}

Response:

execution_id

status

result

trace

List Executions
GET /workflow/executions

Returns historical execution summaries.

Execution Details
GET /workflow/executions/{execution_id}

Returns:

Execution metadata

Node outputs

Full execution trace

##  Example Execution Output
```
{
  "execution_id": "uuid",
  "status": "completed",
  "result": {
    "add_node": { ... },
    "multiply_node": { ... },
    "llm_node": { ... }
  },
  "trace": [
    { "node": "add_node", "status": "completed" },
    { "node": "multiply_node", "status": "completed" },
    { "node": "llm_node", "status": "completed" }
  ]
}
```
##  Tech Stack
Backend

Python

FastAPI

asyncio

SQLite

Pydantic

Uvicorn

Frontend

React (Vite)

TypeScript

REST APIs

##  Engineering Concepts Demonstrated

Directed Acyclic Graph scheduling

Async concurrency control

Lock-based shared state protection

Failure handling patterns

Retry backoff strategies

Deterministic execution pipelines

Persistence abstraction

Execution trace observability

Control plane architecture

##  Project Phases
### Phase 1–2

Basic workflow execution

Node mapping & dependency validation

### Phase 3–4

Conditional nodes

Parallel execution

### Phase 5–6

Retry & timeout policies

Failure state handling

### Phase 7

Persistence layer

Execution history APIs

### Phase 8

React dashboard

Execution detail view

### Phase 9

Async observability improvements

Trace visualization

Dark-mode enterprise UI

##  Design Principles

Deterministic execution first

No silent failures

Observable by default

Async-safe state management

Enterprise-ready audit trail

Separation of concerns

Control plane over chaos

##  How to Run Locally
Backend
cd backend
```
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

uvicorn apps.api.main:app --reload
```

Runs at:

```http://127.0.0.1:8000```

## Swagger:

```http://127.0.0.1:8000/docs```
Frontend
cd frontend

npm install
npm run dev

Create .env:

VITE_BACKEND_URL=http://127.0.0.1:8000

## Runs at:

http://localhost:5173
### Intended Use Cases

Enterprise AI workflow automation

LLM + tool orchestration

Multi-step AI pipelines

Internal AI platforms

Agent-like execution systems

AI infrastructure engineering teams

Compliance-ready AI systems

## 🏆 Project Outcome

This project demonstrates the ability to:

Build async workflow execution engines

Design enterprise AI orchestration systems

Implement retry & failure safety controls

Create audit-ready AI execution logs

Develop full-stack AI infrastructure

Apply system design principles to AI pipelines

##  Author

Sreeja Reddy

AI Engineer focused on:

AI Workflow Orchestration

Enterprise LLM Infrastructure

Graph-based Reasoning Systems

GenAI Governance & Observability

GitHub:
https://github.com/Sreeja-Reddy-0612

LinkedIn:
https://www.linkedin.com/in/sreeja-reddy-5ab708288/
