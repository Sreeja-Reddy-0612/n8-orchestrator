from core.nodes.base_node import BaseNode


class LLMNode(BaseNode):
    def run(self, state: dict):
        prompt = self.config.get("prompt", "")

        output = {
            "response": f"LLM processed: {prompt}"
        }

        state[self.name] = output

        trace_entry = {
            "node": self.name,
            "type": "llm",
            "prompt": prompt,
            "output": output,
        }

        return output, trace_entry, self.next