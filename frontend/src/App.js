import Board from "./Components/Board";
import InstruccionesForm from "./Components/InstruccionesForm";
import './App.css'
function App() {
  return (
      <div >
          <div className="container">
              <h1 className="neon-text">BOOME</h1>
          </div>
          <InstruccionesForm/>
          <Board/>
      </div>

  )
}

export default App;
