import { useState } from "react";

export default function EmergencyForm() {
  const [symptoms, setSymptoms] = useState("");
  const [result, setResult] = useState(null);

  const API_URL = "https://your-backend-url.onrender.com/emergency";

  const handleSubmit = async () => {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ symptoms })
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h1>🚑 IHTN Emergency System</h1>

      <input
        value={symptoms}
        onChange={(e) => setSymptoms(e.target.value)}
        placeholder="Enter symptoms..."
        style={{ padding: "10px", width: "300px" }}
      />

      <button onClick={handleSubmit} style={{ marginLeft: "10px" }}>
        Send Emergency
      </button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Severity: {result.severity}</h3>
          <h3>Hospital: {result.hospital}</h3>
        </div>
      )}
    </div>
  );
}
