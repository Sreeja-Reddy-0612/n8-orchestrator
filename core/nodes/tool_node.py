from typing import Dict, Any
from .base_node import BaseNode
from core.tools.registry import tool_registry
from core.tools.permissions import ToolPermissionManager
import core.tools.builtins  # ensures builtin tools register


class ToolNode(BaseNode):

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:

        tool_name = self.config.get("tool")
        tool_args = self.config.get("args", {})

        permission_manager = ToolPermissionManager(
            allowed_tools=self.config.get("allowed_tools", [])
        )

        permission_manager.validate(tool_name)

        tool_function = tool_registry.get(tool_name)

        state = tool_function(state, **tool_args)

        state.setdefault("trace", [])
        state["trace"].append({
            "node": self.name,
            "type": "tool",
            "tool_invoked": tool_name
        })

        return state