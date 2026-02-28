import { useState } from "react";
import API from "../services/api";

export default function ExecuteWorkflow() {
  const [executionId, setExecutionId] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const runWorkflow = async () => {
    setLoading(true);

    const payload = {
      workflow_name: "tool_test",
      start_at: "tool1",
      nodes: [
        {
          name: "tool1",
          type: "tool",
          config: {
            tool: "math_add",
            args: { a: 5, b: 7 },
          },
          next: null,
        },
      ],
    };

    try {
      const res = await API.post("/workflow/execute", payload);
      setExecutionId(res.data.execution_id);
    } catch (err) {
      alert("Execution failed");
    }

    setLoading(false);
  };

  return (
    <div>
      <h2>Execute Workflow</h2>
      <button onClick={runWorkflow} disabled={loading}>
        {loading ? "Running..." : "Run Workflow"}
      </button>

      {executionId && (
        <p>
          Execution ID: <strong>{executionId}</strong>
        </p>
      )}
    </div>
  );
}