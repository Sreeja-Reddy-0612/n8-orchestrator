import uuid
from typing import Dict


class InMemoryExecutionStore:

    def __init__(self):
        self._store: Dict[str, dict] = {}

    def create_execution(self, workflow_def: dict):
        execution_id = str(uuid.uuid4())

        self._store[execution_id] = {
            "execution_id": execution_id,
            "workflow": workflow_def,
            "status": "running",
            "result": None
        }

        return execution_id

    def complete_execution(self, execution_id: str, result: dict):
        if execution_id in self._store:
            self._store[execution_id]["status"] = "completed"
            self._store[execution_id]["result"] = result

    def get_execution(self, execution_id: str):
        return self._store.get(execution_id)

    def list_executions(self):
        return list(self._store.values())


execution_store = InMemoryExecutionStore()