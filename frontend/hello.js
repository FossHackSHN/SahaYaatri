async function call() {
  const res = await fetch(
    "https://e4a9ba33-8863-44a3-8d32-44f1e9461eb4-00-10r67gl7xdrw5.worf.replit.dev/bus_routes",
    {
      "method": "POST",
      headers:{
        "Content-Type":"application/json"
      },
      body: JSON.stringify({
        "source": "ALUVA",
        "destination": "KALADY",
      }),
    }
  );
  console.log(await res.json());
}

call();
