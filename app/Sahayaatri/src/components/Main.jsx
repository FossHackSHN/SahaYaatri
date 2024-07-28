import { useState } from "react";
import SearchPage from "./SearchPage";
import RouteListPage from "./RouteListPage";

function Main({onRouteChange}) {
  const [routes, setRoutes] = useState([]);

  function onUpdateRoutes(routes){
    setRoutes(routes);
    onRouteChange(routes);
  }

  return (
    <main className="main">
      <div className="container">
        {routes.length == 0 ? (
          <SearchPage setRoutes={onUpdateRoutes} />
        ) : (
          <div>
            {routes.map((route) => (
              <RouteListPage paths={route.route} name={route.name} key={route.name}/>
            ))}
          </div>
        )}
      </div>
    </main>
  );
}

export default Main;
