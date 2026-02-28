import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import API from "../services/api";

interface Execution {
  execution_id: string;
  status: string;
  result: any;
  trace: any;
}

export default function ExecutionDetail() {
  const { id } = useParams<{ id: string }>();
  const [execution, setExecution] = useState<Execution | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchExecution = async () => {
      try {
        const res = await API.get(`/workflow/executions/${id}`);
        setExecution(res.data);
      } catch (error) {
        console.error("Error fetching execution:", error);
      } finally {
        setLoading(false);
      }
    };

    if (id) {
      fetchExecution();
    }
  }, [id]);

  if (loading) return <p style={{ padding: "20px" }}>Loading...</p>;

  if (!execution)
    return <p style={{ padding: "20px" }}>Execution not found.</p>;

  return (
    <div style={{ padding: "20px" }}>
      <h2>Execution Detail</h2>

      <p>
        <strong>ID:</strong> {execution.execution_id}
      </p>

      <p>
        <strong>Status:</strong> {execution.status}
      </p>

      <h3>Result</h3>
      <pre>{JSON.stringify(execution.result, null, 2)}</pre>

      <h3>Trace</h3>
      <pre>{JSON.stringify(execution.trace, null, 2)}</pre>
    </div>
  );
}