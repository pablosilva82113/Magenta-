import React, { useState } from 'react';
import axios from 'axios';

function InstruccionesForm() {
    const [instrucciones, setInstrucciones] = useState('');

    const handleEnviarInstrucciones = async () => {
        try {
            // Envía las instrucciones a FastAPI
            await axios.post('http://localhost:8000/cargar_instrucciones', {
                instrucciones: instrucciones.split('\n').map(linea => linea.split(' '))
            });
        } catch (error) {

            console.error('Error al enviar instrucciones:', error);
        }
    };

    return (
        <div className={"container d-flex flex-column align-items-center"}>
  <textarea
      rows="10"
      cols="50"
      placeholder="Ingresa las instrucciones"
      value={instrucciones}
      onChange={(e) => setInstrucciones(e.target.value)}
      className="text-center"
  />
            <button type="button" className="btn btn-primary mt-3" onClick={handleEnviarInstrucciones}>
                Cargar Instrucciones
            </button>
        </div>

    );
}

export default InstruccionesForm;
