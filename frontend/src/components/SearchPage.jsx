import { useState } from "react";
import BusStopTypeahead from "./BusStopTypeahead";
import { API_URL } from "../data/variables";

function SearchPage({ setRoutes }) {
  const [from, setFrom] = useState("");
  const [to, setTo] = useState("");

  async function searchRoute(e) {
    e.preventDefault();
    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          source: from,
          destination: to,
        }),
      });
      if (res.ok) {
        const data = await res.json();
        setRoutes(data.bus_routes);
        // setRoutes(data);
      } else {
        console.log("Unable to fetch data!!!");
        console.log(res);
        setRoutes([]);
      }
    } catch (e) {
      console.log(e);
      setRoutes([]);
    }
  }

  return (
    <form className="find-form" onSubmit={searchRoute}>
      <BusStopTypeahead
        id="from"
        placeholder="Select the starting stop"
        label="From"
        onChange={(val) => setFrom(val)}
      />
      <BusStopTypeahead
        id="to"
        placeholder="Select the destination stop"
        label="To"
        onChange={(val) => setTo(val)}
      />
      <button type="submit" className="find-button">
        Search
      </button>
    </form>
  );
}

export default SearchPage;
