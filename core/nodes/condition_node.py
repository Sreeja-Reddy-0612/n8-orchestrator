from typing import Dict, Any
from .base_node import BaseNode


class ConditionNode(BaseNode):

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        key = self.config.get("condition_key")
        equals = self.config.get("equals")

        value = state.get(key)

        state.setdefault("trace", [])
        state["trace"].append({
            "node": self.name,
            "type": "condition",
            "evaluated_key": key,
            "value": value
        })

        state["_condition_result"] = (value == equals)

        return state