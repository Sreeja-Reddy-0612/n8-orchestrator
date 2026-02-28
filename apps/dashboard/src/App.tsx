import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import ExecutionDetail from "./pages/ExecutionDetail";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/execution/:id" element={<ExecutionDetail />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;