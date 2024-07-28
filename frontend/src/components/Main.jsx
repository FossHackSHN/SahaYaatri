import { useState } from "react";
import BusStopTypeahead from "./BusStopTypeahead";

function Main() {
  const [from,setFrom]=useState("");
  const [to,setTo]=useState("");

  function searchRoute(){
    try{
      
    }catch{

    }finally{

    }
  }

  return (
    <main className="main">
      <div className="container">
        <form className="find-form">
          <BusStopTypeahead
            id="from"
            placeholder="Select the starting stop"
            label="From"
            onChange={(val)=>setFrom(val)}
          />
          <BusStopTypeahead
            id="to"
            placeholder="Select the destination stop"
            label="To"
            onChange={(val)=>setTo(val)}
          />
          <button type="submit" className="find-button" onClick={searchRoute}>Find</button>
        </form>
      </div>
    </main>
  );
}

export default Main;
