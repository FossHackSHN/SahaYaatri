import { useState } from "react";
import Header from "./components/Header";
import SideMenu from "./components/SideMenu";
import Main from "./components/Main"
import Footer from "./components/Footer"

function App() {
  return (
  <div className="app">
    <Header title={"Sahayathri"}/>
    {/* <SideMenu></SideMenu> */}
    <Main/>
    <Footer/>
  </div>
  );
}

export default App;
