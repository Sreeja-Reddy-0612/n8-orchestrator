from core.nodes.base_node import BaseNode


class ToolNode(BaseNode):
    def run(self, state: dict):
        tool_name = self.config.get("tool")
        args = self.config.get("args", {})

        if tool_name == "math_add":
            result = {"sum": args["a"] + args["b"]}

        elif tool_name == "math_multiply":
            result = {"product": args["a"] * args["b"]}

        else:
            raise Exception(f"Unknown tool: {tool_name}")

        state[self.name] = result

        trace_entry = {
            "node": self.name,
            "type": "tool",
            "tool_invoked": tool_name,
            "output": result,
        }

        return result, trace_entry, self.next