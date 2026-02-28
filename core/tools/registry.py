from typing import Dict, Callable


class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    def register(self, name: str, func: Callable):
        self._tools[name] = func

    def get(self, name: str):
        if name not in self._tools:
            raise Exception(f"Tool not registered: {name}")
        return self._tools[name]

    def list_tools(self):
        return list(self._tools.keys())


tool_registry = ToolRegistry()