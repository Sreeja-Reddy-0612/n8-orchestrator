import { useEffect, useState } from "react";
import API from "../services/api";

interface Props {
  executionId: string;
}

export default function ExecutionDetail({ executionId }: Props) {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    fetchDetail();
  }, []);

  const fetchDetail = async () => {
    const res = await API.get(`/workflow/executions/${executionId}`);
    setData(res.data);
  };

  if (!data) return <p>Loading...</p>;

  return (
    <div>
      <h3>Execution Detail</h3>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}