from typing import Dict, Any, List
from core.nodes.tool_node import ToolNode
from core.workflow_engine.state_manager import StateManager


class WorkflowExecutor:

    NODE_TYPE_MAP = {
        "tool": ToolNode
    }

    def __init__(self, workflow_def: Dict[str, Any]):
        self.workflow_def = workflow_def
        self.nodes = self._build_nodes()

    def _build_nodes(self) -> List:
        nodes = []

        for node_def in self.workflow_def.get("nodes", []):
            node_type = node_def["type"]
            node_name = node_def["name"]
            config = node_def.get("config", {})

            node_class = self.NODE_TYPE_MAP.get(node_type)

            if not node_class:
                raise ValueError(f"Unsupported node type: {node_type}")

            nodes.append(node_class(node_name, config))

        return nodes

    def execute(self) -> Dict[str, Any]:
        state = StateManager.initialize()

        for node in self.nodes:
            state = node.execute(state)

        return state