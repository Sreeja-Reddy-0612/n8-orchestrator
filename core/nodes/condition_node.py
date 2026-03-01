def execute_condition_node(node, state):

    config = node["config"]
    variable = config["variable"]
    operator = config["operator"]
    compare_to = config["value"]

    if variable not in state:
        raise Exception(f"Dependency '{variable}' not found in state.")

    previous_output = state[variable]

    # Extract nested tool output safely
    value = previous_output.get("output", {}).get("sum")

    if value is None:
        raise Exception(f"No 'sum' found in output of '{variable}'.")

    if operator == ">":
        result = value > compare_to
    elif operator == "<":
        result = value < compare_to
    elif operator == "==":
        result = value == compare_to
    else:
        raise Exception("Unsupported operator")

    output = {
        "node": node["name"],
        "type": "condition",
        "evaluated": {
            "variable": variable,
            "value": value,
            "operator": operator,
            "compare_to": compare_to,
            "result": result
        }
    }

    return output