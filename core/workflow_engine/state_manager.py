from typing import Dict, Any


class StateManager:
    """
    Handles workflow state initialization and mutation.
    """

    @staticmethod
    def initialize() -> Dict[str, Any]:
        return {
            "messages": [],
            "metadata": {}
        }