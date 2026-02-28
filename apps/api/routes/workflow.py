from fastapi import APIRouter
from core.nodes.executor import WorkflowExecutor
from core.persistence.checkpoint import (
    save_execution,
    get_execution,
    list_executions
)

router = APIRouter(prefix="/workflow")


@router.post("/execute")
def execute_workflow(workflow: dict):
    executor = WorkflowExecutor(workflow)
    result = executor.run()

    save_execution(result)

    return result


@router.get("/executions")
def get_executions():
    return list_executions()


@router.get("/executions/{execution_id}")
def get_execution_by_id(execution_id: str):
    return get_execution(execution_id)