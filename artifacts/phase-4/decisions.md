# Phase 4 – Architectural Decisions

## 1. Framework Choice
Frontend: React + Vite
Backend: FastAPI

Reason:
- Fast development speed
- Clean API integration
- Lightweight stack

---

## 2. Polling vs WebSockets
Decision: Polling (2-second interval)

Reason:
- Simpler implementation
- Suitable for Phase 4
- WebSockets planned for Phase 6

---

## 3. State Management
Decision: Local React state

Reason:
- No need for Redux yet
- Small system
- Keep architecture minimal

---

## 4. Execution Store
Decision: In-memory store

Reason:
- Rapid prototyping
- Will migrate to Postgres in Phase 5

---

## 5. CORS Strategy
Restricted to localhost:5173

Reason:
- Development environment only
- Secure by default