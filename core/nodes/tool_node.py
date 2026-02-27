from typing import Dict, Any
from .base_node import BaseNode


class ToolNode(BaseNode):

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        message = self.config.get("message", "")

        state.setdefault("messages", [])
        state["messages"].append(
            {
                "node": self.name,
                "message": message
            }
        )

        return state