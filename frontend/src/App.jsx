import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [path, setPath] = useState('');
  const [secret, setSecret] = useState(null)
  const [error, setError] = useState(null)

  const fetchSecret = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/api/secrets", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ path }), // Enviar el path como JSON 
      });

      if(!response.ok){
        throw new Error("Failed to fetch secret");
      }

      const data = await response.json();
      setSecret(data);
      setError(null);
    } catch (err){
      setError(err.message);
      setSecret(null);
    }
  };

  return (
    <div>
      <h1>Secret Manager</h1>
      <input
        type="text"
        placeholder="Enter secret path"
        value={path}
        onChange={(e) => setPath(e.target.value)}
      />
      <button onClick={fetchSecret}>Fetch Secret</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {secret && <pre>{JSON.stringify(secret, null, 2)}</pre>}
    </div>
  );
}

export default App
