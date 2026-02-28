def math_tool(state, **kwargs):
    a = kwargs.get("a", 0)
    b = kwargs.get("b", 0)
    result = a + b

    state.setdefault("messages", [])
    state["messages"].append({
        "node": "math_tool",
        "message": f"Result: {result}"
    })

    state["math_result"] = result
    return state