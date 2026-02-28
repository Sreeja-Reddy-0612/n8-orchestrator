class WorkflowParser:

    def __init__(self, workflow_def: dict):
        self.workflow_def = workflow_def

    def parse_nodes(self):
        nodes = {}

        for node in self.workflow_def.get("nodes", []):
            nodes[node["name"]] = node

        return nodes