from fastapi import FastAPI
from apps.api.lifecycle import register_lifecycle_events
from apps.api.routes.workflow import router as workflow_router

app = FastAPI(
    title="N8 Orchestrator - Phase 3",
    version="0.3.0"
)

register_lifecycle_events(app)

app.include_router(workflow_router)


@app.get("/")
def root():
    return {"status": "N8 Orchestrator running"}