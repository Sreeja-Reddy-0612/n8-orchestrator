from core.tools.registry import tool_registry
from .echo_tool import echo_tool
from .math_tool import math_tool


def register_builtin_tools():
    tool_registry.register("echo", echo_tool)
    tool_registry.register("math_add", math_tool)