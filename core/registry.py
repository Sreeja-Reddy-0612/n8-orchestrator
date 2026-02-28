from core.nodes.tool_node import ToolNode
from core.nodes.llm_node import LLMNode
from core.nodes.condition_node import ConditionNode

NODE_REGISTRY = {
    "tool": ToolNode,
    "llm": LLMNode,
    "condition": ConditionNode,
}