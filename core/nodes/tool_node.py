def execute_tool_node(node, state):

    config = node["config"]
    tool_name = config["tool"]
    args = config.get("args", {})

    if tool_name == "math_add":
        a = args.get("a", 0)
        b = args.get("b", 0)
        result = {"sum": a + b}
    else:
        raise Exception(f"Unknown tool: {tool_name}")

    output = {
        "node": node["name"],
        "type": "tool",
        "tool_invoked": tool_name,
        "output": result
    }

    return output