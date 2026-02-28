import { useState } from "react";
import { executeWorkflow } from "../services/api";

function ExecuteWorkflow() {
  const [loading, setLoading] = useState(false);

  const handleRun = async () => {
    if (loading) return;

    setLoading(true);

    try {
      await executeWorkflow();
      alert("Workflow executed successfully");
    } catch (error) {
      alert("Execution failed");
    }

    setLoading(false);
  };

  return (
    <div>
      <button onClick={handleRun} disabled={loading}>
        {loading ? "Running..." : "Run Workflow"}
      </button>
    </div>
  );
}

export default ExecuteWorkflow;