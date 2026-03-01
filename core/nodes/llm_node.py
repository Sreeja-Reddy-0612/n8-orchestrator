def execute_llm_node(node, state):

    prompt = node["config"]["prompt"]

    response = f"LLM processed: {prompt}"

    output = {
        "node": node["name"],
        "type": "llm",
        "prompt": prompt,
        "output": {
            "response": response
        }
    }

    return output