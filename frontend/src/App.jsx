import { useEffect, useState } from "react";
import Header from "./components/Header";
import SideMenu from "./components/SideMenu";
import Main from "./components/Main";
import Footer from "./components/Footer";

function App() {
  const [routes, setRoutes] = useState([]);

  useEffect(() => {
    console.log(routes);
  }, [routes]);

  function clearRoutes() {
    setRoutes([]);
  }

  return (
    <div className="app">
      <Header title={"Sahayaatri"} isMainPage={routes.length !== 0} />
      {/* <SideMenu></SideMenu> */}
      <Main onRouteChange={(data) => setRoutes(data)} />
      <Footer />
    </div>
  );
}

export default App;
