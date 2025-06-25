import json
import os

RUTA = "puntajes.json"

def obtener_top_puntajes():
    if not os.path.exists(RUTA):
        return []
    with open(RUTA, "r") as f:
        data = json.load(f)
    return sorted([(x["nombre"], x["puntaje"]) for x in data], key=lambda x: x[1], reverse=True)[:5]

def guardar_puntaje(nombre, puntos):
    nuevo = {"nombre": nombre, "puntaje": puntos}
    if os.path.exists(RUTA):
        with open(RUTA, "r") as f:
            data = json.load(f)
    else:
        data = []
    data.append(nuevo)
    with open(RUTA, "w") as f:
        json.dump(data, f)
