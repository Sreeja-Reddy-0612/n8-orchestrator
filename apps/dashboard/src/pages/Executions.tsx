import { useEffect, useState } from "react";
import API from "../services/api";

interface Execution {
  execution_id: string;
  status: string;
}

export default function Executions() {
  const [executions, setExecutions] = useState<Execution[]>([]);

  const fetchExecutions = async () => {
    const res = await API.get("/workflow/executions");
    setExecutions(res.data);
  };

  useEffect(() => {
    fetchExecutions();

    // Auto-refresh every 2 seconds (temporary for Phase 4)
    const interval = setInterval(fetchExecutions, 2000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h2>Execution History</h2>

      {executions.length === 0 && <p>No executions yet.</p>}

      {executions.map((e) => (
        <div key={e.execution_id}>
          <strong>{e.execution_id}</strong> — {e.status}
        </div>
      ))}
    </div>
  );
}