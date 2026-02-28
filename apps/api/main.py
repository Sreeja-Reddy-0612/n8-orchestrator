from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.api.lifecycle import register_lifecycle_events
from apps.api.routes.workflow import router as workflow_router

app = FastAPI(
    title="N8 Orchestrator - Phase 4",
    version="0.4.0"
)

# ✅ CORS Middleware (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_lifecycle_events(app)

app.include_router(workflow_router)


@app.get("/")
def root():
    return {"status": "N8 Orchestrator running"}