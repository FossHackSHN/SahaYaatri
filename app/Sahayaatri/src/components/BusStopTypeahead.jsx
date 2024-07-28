import { Typeahead } from "react-bootstrap-typeahead";
import ToggleButton from "../components/ToggleButton";
import stations from "../data/station";
import "bootstrap/dist/css/bootstrap.css";

function BusStopTypeahead({ id,placeholder,label,onChange }) {
  function filterBy(station, state) {
    if (state.selected.length) {
      return true;
    }
    return station.toLowerCase().indexOf(state.text.toLowerCase()) > -1;
  }

  return (
    <div className="typeahead">
    <label>{label}</label>
    <Typeahead
      id={id}
      filterBy={filterBy}
      options={stations}
      placeholder={placeholder}
      onChange={(arr)=>onChange(arr.length?arr.at(0):"")}
    >
      {({ isMenuShown, toggleMenu }) => (
        <ToggleButton isOpen={isMenuShown} onClick={(e) => toggleMenu()} />
      )}
    </Typeahead>
    </div>
  );
}

export default BusStopTypeahead;
