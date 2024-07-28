const ToggleButton = ({ isOpen, onClick }) => (
  <button
    className="toggle-button"
    onClick={onClick}
    onMouseDown={(e) => {
      e.preventDefault();
    }}
  >
    {isOpen ? "▲" : "▼"}
  </button>
);

export default ToggleButton;
