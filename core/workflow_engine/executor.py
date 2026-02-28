from core.workflow_engine.parser import WorkflowParser
from core.nodes.tool_node import ToolNode
from core.nodes.condition_node import ConditionNode
from core.nodes.llm_node import LLMNode


NODE_TYPE_MAP = {
    "tool": ToolNode,
    "condition": ConditionNode,
    "llm": LLMNode,
}


class WorkflowExecutor:

    def __init__(self, workflow_def):
        self.workflow_def = workflow_def
        self.parser = WorkflowParser(workflow_def)

    def execute(self):

        nodes = self.parser.parse_nodes()
        current_node_name = self.workflow_def.get("start_at")
        state = {"messages": [], "trace": []}

        step_count = 0
        MAX_STEPS = 50   # safety guard

        while current_node_name:

            if step_count > MAX_STEPS:
                raise Exception("Max step limit exceeded (possible infinite loop)")

            node_def = nodes.get(current_node_name)

            if not node_def:
                raise Exception(f"Node not found: {current_node_name}")

            node_class = NODE_TYPE_MAP.get(node_def["type"])
            if not node_class:
                raise Exception(f"Unsupported node type: {node_def['type']}")

            node_instance = node_class(node_def["name"], node_def.get("config", {}))

            state = node_instance.execute(state)

            # Determine next node
            if node_def["type"] == "condition":
                current_node_name = state.get("next_node")
            else:
                current_node_name = node_def.get("next")

            step_count += 1

        return {
            "status": "success",
            "result": state
        }