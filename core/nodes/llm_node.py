from typing import Dict, Any
from .base_node import BaseNode
from openai import OpenAI
from apps.api.config import OPENAI_API_KEY


class LLMNode(BaseNode):

    def __init__(self, name, config):
        super().__init__(name, config)
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def execute(self, state: Dict[str, Any]) -> Dict[str, Any]:

        prompt = self.config.get("prompt", "")

        response = self.client.chat.completions.create(
            model=self.config.get("model", "gpt-4o-mini"),
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.choices[0].message.content

        state.setdefault("messages", [])
        state["messages"].append({
            "node": self.name,
            "message": output
        })

        state.setdefault("trace", [])
        state["trace"].append({
            "node": self.name,
            "type": "llm",
            "model": self.config.get("model", "gpt-4o-mini")
        })

        return state