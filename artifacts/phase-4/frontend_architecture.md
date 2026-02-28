# Phase 4 – Frontend Integration Architecture

## Objective
Introduce a React-based control plane dashboard for triggering and monitoring workflows.

---

## Architecture Flow

Browser (React Dashboard)
        ↓
Axios API Layer
        ↓
FastAPI Backend
        ↓
Workflow Executor
        ↓
Execution Store (In-Memory)
        ↓
Response Returned to UI

---

## Key Components

### 1. Dashboard UI
- Run Workflow Button
- Execution ID display
- Execution History List
- Auto-refresh (2s polling)

### 2. API Service Layer
File: src/services/api.ts

- Axios instance
- Base URL: http://127.0.0.1:8000

### 3. Workflow Execution Trigger
POST /workflow/execute

Returns:
{
  "execution_id": "<uuid>",
  "status": "completed"
}

### 4. Execution History
GET /workflow/executions

Returns:
[
  {
    "execution_id": "...",
    "status": "completed"
  }
]

---

## Cross-Origin Setup

CORS middleware enabled in FastAPI:

allow_origins=["http://localhost:5173"]

This allows frontend-backend communication.

---

## Current Limitations

- Polling instead of WebSockets
- In-memory persistence (not durable)
- No execution details page
- No multi-tenant support

---

Phase 4 Status: COMPLETE