from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import json
import bvm
import gramar
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
obvm = bvm.BMV()
obvm.NoLinnea = 0
obvm.Salto = False
obvm.Programa = []


class Instruccion(BaseModel):
    instrucciones: List[List[str]]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/cargar_instrucciones")
async def cargar_instrucciones(json_data: dict):
    instrucciones = json_data.get("instrucciones", [])
    obvm.Programa = instrucciones
    obvm.NoLinnea = 0
    obvm.Salto = False
    return {"message": "Instrucciones cargadas correctamente"}

@app.get("/ejecutar_instrucciones")
async def ejecutar_instrucciones():
    resultado = []
    while obvm.NoLinnea < len(obvm.Programa):
        if not obvm.Salto:
            linea = obvm.Programa[obvm.NoLinnea]
            r = gramar.lienacodigo(linea)

            if r:
                obvm.depurar()
                resultado.append({
                    "Pos X":obvm.X,
                    "Pos Y":obvm.Y,
                    "Ejecutando línea": obvm.NoLinnea
                })
                obvm.ejecutarCodigo(linea)
                #resultado.append({"Salto": obvm.Salto})

            if not obvm.Salto:
                obvm.NoLinnea += 1
            else:
                obvm.Salto = False

    return {"resultado": resultado}    


@app.get("/depurar")
def depurar_instrucciones():
    obvm.depurar()
    return {"mensaje": "Instrucciones depuradas"}

 