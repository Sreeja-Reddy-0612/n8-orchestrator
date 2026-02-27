from fastapi import FastAPI
from apps.api.routes import workflow

app = FastAPI(title="N8 Orchestrator - Phase 1")

app.include_router(workflow.router, prefix="/workflow", tags=["Workflow"])


@app.get("/")
def health():
    return {"status": "running"}