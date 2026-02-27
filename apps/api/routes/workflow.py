from fastapi import APIRouter, HTTPException
from core.workflow_engine.executor import WorkflowExecutor

router = APIRouter()


@router.post("/execute")
def execute_workflow(workflow: dict):
    try:
        executor = WorkflowExecutor(workflow)
        result = executor.execute()
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))