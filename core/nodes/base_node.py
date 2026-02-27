from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseNode(ABC):
    """
    Abstract base node for all workflow nodes.
    """

    def __init__(self, name: str, config: Dict[str, Any]):
        self.name = name
        self.config = config

    @abstractmethod
    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:
        pass