import yaml
from typing import Dict, Any


class WorkflowParser:
    """
    Parses YAML workflow definition into Python dictionary.
    """

    @staticmethod
    def parse_yaml(file_path: str) -> Dict[str, Any]:
        with open(file_path, "r") as f:
            data = yaml.safe_load(f)
        return data