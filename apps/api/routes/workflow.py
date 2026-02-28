from fastapi import APIRouter, HTTPException
from core.workflow_engine.executor import WorkflowExecutor

router = APIRouter()


@router.post("/workflow/execute")
def execute_workflow(payload: dict):
    try:
        executor = WorkflowExecutor(payload)
        result = executor.execute()   # <-- CHANGE HERE
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))