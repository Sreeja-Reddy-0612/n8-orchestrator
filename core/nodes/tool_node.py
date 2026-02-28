class ToolNode:
    def __init__(self, node_def):
        self.node_def = node_def

    def execute(self):
        config = self.node_def.get("config", {})
        tool_name = config.get("tool")
        args = config.get("args", {})

        if tool_name == "math_add":
            return self.math_add(args)

        raise Exception(f"Unknown tool: {tool_name}")

    def math_add(self, args):
        a = args.get("a", 0)
        b = args.get("b", 0)
        return {"sum": a + b}