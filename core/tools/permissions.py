class ToolPermissionManager:

    def __init__(self, allowed_tools=None):
        self.allowed_tools = allowed_tools or []

    def validate(self, tool_name: str):
        if self.allowed_tools and tool_name not in self.allowed_tools:
            raise Exception(f"Tool not permitted: {tool_name}")