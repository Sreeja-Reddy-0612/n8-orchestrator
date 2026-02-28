from typing import Dict, Any
from core.nodes.tool_node import ToolNode
from core.nodes.condition_node import ConditionNode
from core.workflow_engine.state_manager import StateManager
from core.workflow_engine.step_guard import StepGuard


class WorkflowExecutor:

    NODE_TYPE_MAP = {
        "tool": ToolNode,
        "condition": ConditionNode
    }

    def __init__(self, workflow_def: Dict[str, Any]):
        self.workflow_def = workflow_def
        self.nodes = {}
        self._build_nodes()

    def _build_nodes(self):
        for node_def in self.workflow_def.get("nodes", []):
            node_type = node_def["type"]
            node_name = node_def["name"]
            config = node_def.get("config", {})

            node_class = self.NODE_TYPE_MAP.get(node_type)

            if not node_class:
                raise ValueError(f"Unsupported node type: {node_type}")

            self.nodes[node_name] = {
                "instance": node_class(node_name, config),
                "definition": node_def
            }

    def execute(self) -> Dict[str, Any]:

        state = StateManager.initialize()
        state["trace"] = []

        current_node_name = self.workflow_def.get("start_at")

        if not current_node_name:
            raise Exception("Workflow must define start_at")

        guard = StepGuard()

        while current_node_name:

            guard.increment()

            node_entry = self.nodes.get(current_node_name)
            if not node_entry:
                raise Exception(f"Node not found: {current_node_name}")

            node_instance = node_entry["instance"]
            node_def = node_entry["definition"]

            state = node_instance.execute(state)

            # Append execution trace
            state["trace"].append({
                "node": current_node_name,
                "type": node_def["type"]
            })

            # Routing logic
            if node_def["type"] == "condition":
                condition_result = state.pop("_condition_result", False)

                if condition_result:
                    current_node_name = node_def.get("on_true")
                else:
                    current_node_name = node_def.get("on_false")
            else:
                current_node_name = node_def.get("next")

        return state