executions_store = {}


def init_db():
    global executions_store
    executions_store = {}


def save_execution(execution: dict):
    executions_store[execution["execution_id"]] = execution


def list_executions():
    return [
        {
            "execution_id": e["execution_id"],
            "status": e["status"]
        }
        for e in executions_store.values()
    ]


def get_execution(execution_id: str):
    return executions_store.get(execution_id)