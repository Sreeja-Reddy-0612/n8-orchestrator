from core.nodes.base_node import BaseNode


class ConditionNode(BaseNode):
    def run(self, state: dict):
        variable = self.config["variable"]
        operator = self.config["operator"]
        value = self.config["value"]
        true_next = self.config["true_next"]
        false_next = self.config["false_next"]

        # Extract numeric value properly
        node_output = state.get(variable)

        if isinstance(node_output, dict):
            # If tool output like {"sum": 15}
            current_value = list(node_output.values())[0]
        else:
            current_value = node_output

        condition_met = False

        if operator == ">":
            condition_met = current_value > value
        elif operator == "<":
            condition_met = current_value < value
        elif operator == "==":
            condition_met = current_value == value

        next_node = true_next if condition_met else false_next

        trace_entry = {
            "node": self.name,
            "type": "condition",
            "evaluated": {
                "variable": variable,
                "value": current_value,
                "operator": operator,
                "compare_to": value,
                "result": condition_met,
            },
        }

        return None, trace_entry, next_node