from typing import Dict, Any


class StateManager:

    @staticmethod
    def initialize() -> Dict[str, Any]:
        return {
            "messages": [],
            "metadata": {},
            "trace": {},
        }