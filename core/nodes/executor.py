import uuid
import time
from core.registry import NODE_REGISTRY
from core.persistence.checkpoint import save_execution


class WorkflowExecutor:

    def __init__(self, workflow: dict):
        self.workflow = workflow
        self.execution_id = str(uuid.uuid4())
        self.state = {}
        self.trace = []
        self.status = "running"

        self.nodes = {
            node["name"]: node
            for node in workflow["nodes"]
        }

        self.MAX_STEPS = 100

    def execute(self):
        current_node_name = self.workflow["start_at"]
        step_count = 0

        try:
            while current_node_name:

                if step_count > self.MAX_STEPS:
                    raise Exception("Max step limit exceeded (possible infinite loop)")

                node_config = self.nodes[current_node_name]
                node_type = node_config["type"]

                node_class = NODE_REGISTRY[node_type]
                node_instance = node_class(node_config)

                # 🔥 Phase 7: Retry + Timeout Support
                result, trace_entry, next_node = self._execute_with_retry(
                    node_instance,
                    node_config
                )

                if trace_entry:
                    self.trace.append(trace_entry)

                current_node_name = next_node
                step_count += 1

            self.status = "completed"

        except Exception as e:
            self.status = "failed"
            self.trace.append({
                "error": str(e)
            })

        # Save execution (success or failure)
        save_execution(
            self.execution_id,
            self.status,
            self.state,
            self.trace
        )

        return {
            "execution_id": self.execution_id,
            "status": self.status,
            "result": self.state,
            "trace": self.trace,
        }

    # 🔥 NEW PHASE 7 METHOD
    def _execute_with_retry(self, node_instance, node_config):

        retry_config = node_config.get("retry", {})
        max_retries = retry_config.get("max_retries", 0)
        delay = retry_config.get("delay_seconds", 0)
        timeout = retry_config.get("timeout_seconds", None)

        attempt = 0

        while True:
            try:
                start_time = time.time()

                result, trace_entry, next_node = node_instance.run(self.state)

                # Timeout check
                if timeout:
                    elapsed = time.time() - start_time
                    if elapsed > timeout:
                        raise Exception(
                            f"Node timeout exceeded ({timeout}s)"
                        )

                return result, trace_entry, next_node

            except Exception as e:
                attempt += 1

                if attempt > max_retries:
                    raise Exception(
                        f"Node failed after {max_retries} retries: {str(e)}"
                    )

                # Add retry trace entry
                self.trace.append({
                    "node": node_config["name"],
                    "retry_attempt": attempt,
                    "error": str(e)
                })

                if delay > 0:
                    time.sleep(delay)