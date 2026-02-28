class BaseNode:
    def __init__(self, config: dict):
        self.name = config["name"]
        self.type = config["type"]
        self.config = config.get("config", {})
        self.next = config.get("next")

    def run(self, state: dict):
        raise NotImplementedError("run() must be implemented by node type")