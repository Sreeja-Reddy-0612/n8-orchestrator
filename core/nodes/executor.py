import uuid
import time

from core.nodes.tool_node import execute_tool_node
from core.nodes.condition_node import execute_condition_node
from core.nodes.llm_node import execute_llm_node


class WorkflowExecutor:

    def __init__(self, workflow):
        self.workflow = workflow
        self.nodes = {node["name"]: node for node in workflow.get("nodes", [])}
        self.state = {}
        self.trace = []
        self.execution_id = str(uuid.uuid4())
        self.completed = set()
        self.failed = set()

    def _execute_node(self, node):

        retry_config = node.get("retry", {})
        max_retries = retry_config.get("max_retries", 0)
        delay_seconds = retry_config.get("delay_seconds", 0)

        attempts = 0

        while attempts <= max_retries:
            try:
                node_type = node["type"]

                if node_type == "tool":
                    result = execute_tool_node(node, self.state)
                elif node_type == "condition":
                    result = execute_condition_node(node, self.state)
                elif node_type == "llm":
                    result = execute_llm_node(node, self.state)
                else:
                    raise Exception(f"Unknown node type: {node_type}")

                # Store full result in state
                self.state[node["name"]] = result
                self.trace.append(result)
                self.completed.add(node["name"])
                return

            except Exception as e:
                attempts += 1

                if attempts > max_retries:
                    self.failed.add(node["name"])
                    self.trace.append({
                        "node": node["name"],
                        "type": node.get("type"),
                        "error": str(e),
                        "status": "failed"
                    })
                    return

                time.sleep(delay_seconds)

    def execute(self):

        total_nodes = len(self.nodes)

        if total_nodes == 0:
            raise Exception("No nodes provided in workflow.")

        while len(self.completed) + len(self.failed) < total_nodes:

            progress_made = False

            for node_name, node in self.nodes.items():

                if node_name in self.completed or node_name in self.failed:
                    continue

                dependencies = node.get("depends_on", [])

                # Validate dependency names exist
                for dep in dependencies:
                    if dep not in self.nodes:
                        raise Exception(f"Dependency '{dep}' not found in workflow nodes.")

                # Execute only when all dependencies are completed
                if all(dep in self.completed for dep in dependencies):
                    self._execute_node(node)
                    progress_made = True

            if not progress_made:
                raise Exception(
                    "Deadlock detected: Circular dependency or unresolved dependencies."
                )

        status = "completed" if not self.failed else "failed"

        return {
            "execution_id": self.execution_id,
            "status": status,
            "result": self.state,
            "trace": self.trace
        }