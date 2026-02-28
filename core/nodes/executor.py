import uuid
from core.registry import NODE_REGISTRY
from core.persistence.checkpoint import save_execution


class WorkflowExecutor:
    def __init__(self, workflow: dict):
        self.workflow = workflow
        self.execution_id = str(uuid.uuid4())
        self.state = {}
        self.trace = []
        self.status = "running"

        # Map nodes by name
        self.nodes = {
            node["name"]: node
            for node in workflow["nodes"]
        }

    def execute(self):
        current_node_name = self.workflow["start_at"]
        step_count = 0
        MAX_STEPS = 50

        try:
            while current_node_name:
                if step_count > MAX_STEPS:
                    raise Exception("Infinite loop detected")

                step_count += 1

                node_config = self.nodes.get(current_node_name)

                if not node_config:
                    raise Exception(f"Node not found: {current_node_name}")

                node_type = node_config["type"]

                node_class = NODE_REGISTRY.get(node_type)

                if not node_class:
                    raise Exception(f"Unsupported node type: {node_type}")

                node_instance = node_class(node_config)

                result, trace_entry, next_node = node_instance.run(self.state)

                if trace_entry:
                    self.trace.append(trace_entry)

                current_node_name = next_node

            self.status = "completed"

        except Exception as e:
            self.status = "failed"
            self.trace.append({"error": str(e)})

        save_execution(
            self.execution_id,
            self.status,
            self.state,
            self.trace
        )

        return {
            "execution_id": self.execution_id,
            "status": self.status,
            "result": self.state,
            "trace": self.trace,
        }