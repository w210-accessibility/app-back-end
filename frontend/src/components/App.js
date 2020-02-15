import React from 'react';
import { render } from "react-dom";
import MapContainer from './MapContainer.js'

function App() {
  return (
    <div>
      <MapContainer />
    </div>
  );
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
