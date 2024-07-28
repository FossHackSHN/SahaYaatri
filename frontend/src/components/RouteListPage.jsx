import { useEffect } from "react";

function RouteListPage({ paths,name }) {
  useEffect(()=>{
    console.log(paths);
  },[]);

  return (
    <table className="table caption-top">
      <caption>{name}</caption>
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Source Departure</th>
          <th scope="col">Destination Arrival</th>
          <th scope="col">Duration</th>
          <th scope="col">Bus No.</th>
        </tr>
      </thead>
      <tbody>
        {paths.map((path, index) => (
          <tr key={index}>
            <th scope="row">{index + 1}</th>
            <td>{path["source_departure"] || "Not Available"}</td>
            <td>{path["destination_arrival"] || "Not Available"}</td>
            <td>{path["duration"] || "Not Available"}</td>
            <td>{path["Vehicle Number"] || "Not Available"}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default RouteListPage;
