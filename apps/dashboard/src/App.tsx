import ExecuteWorkflow from "./pages/ExecuteWorkflow";
import Executions from "./pages/Executions";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>N8 Orchestrator Dashboard</h1>

      <ExecuteWorkflow />

      <hr />

      <Executions />
    </div>
  );
}

export default App;