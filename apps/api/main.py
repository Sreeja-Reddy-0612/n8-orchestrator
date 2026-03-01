from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.api.routes.workflow import router as workflow_router
from core.persistence.checkpoint import init_db

app = FastAPI(
    title="N8 Orchestrator - Phase 8",
    version="0.8.0"
)

# ✅ CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize in-memory or DB storage
init_db()

# Register routes
app.include_router(workflow_router)


@app.get("/")
def root():
    return {"status": "N8 Orchestrator Phase 8 running"}