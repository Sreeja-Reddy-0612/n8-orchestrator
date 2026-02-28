import uuid
from core.nodes.tool_node import ToolNode


class WorkflowExecutor:
    def __init__(self, workflow_def):
        self.workflow_def = workflow_def
        self.execution_id = str(uuid.uuid4())
        self.trace = []
        self.result = {}
        self.status = "running"

    def run(self):
        try:
            start_node_name = self.workflow_def.get("start_at")
            nodes = {
                node["name"]: node
                for node in self.workflow_def.get("nodes", [])
            }

            current_node = nodes.get(start_node_name)

            while current_node:
                node_type = current_node.get("type")

                if node_type == "tool":
                    tool_node = ToolNode(current_node)
                    output = tool_node.execute()

                    self.trace.append({
                        "node": current_node["name"],
                        "type": "tool",
                        "tool_invoked": current_node["config"]["tool"],
                        "output": output
                    })

                    self.result[current_node["name"]] = output

                next_node = current_node.get("next")
                current_node = nodes.get(next_node) if next_node else None

            self.status = "completed"

        except Exception as e:
            self.status = "failed"
            self.trace.append({
                "error": str(e)
            })

        return {
            "execution_id": self.execution_id,
            "status": self.status,
            "result": self.result,
            "trace": self.trace
        }