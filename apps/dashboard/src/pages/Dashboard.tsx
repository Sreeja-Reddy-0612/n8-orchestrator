import { useEffect, useState } from "react";
import API from "../services/api";
import { Link } from "react-router-dom";

interface Execution {
  execution_id: string;
  status: string;
}

export default function Dashboard() {
  const [executionId, setExecutionId] = useState<string | null>(null);
  const [executions, setExecutions] = useState<Execution[]>([]);
  const [loading, setLoading] = useState(false);

  const runWorkflow = async () => {
    setLoading(true);

    const payload = {
      workflow_name: "math_workflow",
      start_at: "tool1",
      nodes: [
        {
          name: "tool1",
          type: "tool",
          config: {
            tool: "math_add",
            args: { a: 10, b: 20 }
          },
          next: null
        }
      ]
    };

    try {
      const res = await API.post("/workflow/execute", payload);
      setExecutionId(res.data.execution_id);
      fetchExecutions();
    } catch (error) {
      console.error("Execution failed:", error);
    } finally {
      setLoading(false);
    }
  };

  const fetchExecutions = async () => {
    try {
      const res = await API.get("/workflow/executions");
      setExecutions(res.data);
    } catch (error) {
      console.error("Fetch executions failed:", error);
    }
  };

  useEffect(() => {
    fetchExecutions();
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>N8 Orchestrator Dashboard</h1>

      <h2>Execute Workflow</h2>
      <button onClick={runWorkflow} disabled={loading}>
        {loading ? "Running..." : "Run Workflow"}
      </button>

      {executionId && (
        <p>
          <strong>Execution ID:</strong> {executionId}
        </p>
      )}

      <hr />

      <h2>Execution History</h2>

      {executions.length === 0 && <p>No executions yet.</p>}

      {executions.map((e) => (
        <div key={e.execution_id}>
          <Link to={`/execution/${e.execution_id}`}>
            {e.execution_id}
          </Link>{" "}
          — {e.status}
        </div>
      ))}
    </div>
  );
}