def echo_tool(state, **kwargs):
    message = kwargs.get("message", "")
    state.setdefault("messages", [])
    state["messages"].append({
        "node": "echo_tool",
        "message": message
    })
    return state