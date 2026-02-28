from fastapi import APIRouter, HTTPException
from core.workflow_engine.executor import WorkflowExecutor
from core.persistence.in_memory_store import execution_store

router = APIRouter()


@router.post("/workflow/execute")
def execute_workflow(payload: dict):

    try:
        execution_id = execution_store.create_execution(payload)

        executor = WorkflowExecutor(payload, execution_id=execution_id)
        result = executor.execute()

        execution_store.complete_execution(execution_id, result)

        return {
            "execution_id": execution_id,
            "status": "completed"
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/workflow/executions")
def list_executions():
    return execution_store.list_executions()


@router.get("/workflow/executions/{execution_id}")
def get_execution(execution_id: str):

    execution = execution_store.get_execution(execution_id)

    if not execution:
        raise HTTPException(status_code=404, detail="Execution not found")

    return execution