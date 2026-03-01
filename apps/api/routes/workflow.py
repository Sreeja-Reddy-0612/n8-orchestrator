from fastapi import APIRouter, HTTPException
from core.nodes.executor import WorkflowExecutor
from core.persistence.checkpoint import (
    save_execution,
    list_executions,
    get_execution,
)

router = APIRouter(prefix="/workflow", tags=["Workflow"])


@router.post("/execute")
def execute_workflow(workflow: dict):
    try:
        executor = WorkflowExecutor(workflow)
        result = executor.execute()

        # 🔥 IMPORTANT: Save execution to persistence layer
        save_execution(result)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/executions")
def get_all_executions():
    return list_executions()


@router.get("/executions/{execution_id}")
def get_execution_by_id(execution_id: str):
    execution = get_execution(execution_id)

    if not execution:
        raise HTTPException(status_code=404, detail="Execution not found")

    return execution