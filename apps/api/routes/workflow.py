from fastapi import APIRouter
from core.nodes.executor import WorkflowExecutor
from core.persistence.checkpoint import list_executions, get_execution

router = APIRouter(prefix="/workflow", tags=["Workflow"])


@router.post("/execute")
def execute_workflow(workflow: dict):
    executor = WorkflowExecutor(workflow)
    result = executor.execute()
    return result


@router.get("/executions")
def get_all_executions():
    return list_executions()


@router.get("/executions/{execution_id}")
def get_execution_by_id(execution_id: str):
    return get_execution(execution_id)