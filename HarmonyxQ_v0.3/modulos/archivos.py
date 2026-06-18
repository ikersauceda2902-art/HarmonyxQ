import os
import json

def cargar_canciones():
    if os.path.exists("datos/canciones.json"):
        print("Cargando datos...")
        with open("datos/canciones.json", "r") as archivo:
            lista_canciones = json.load(archivo)
            return lista_canciones
    else:
        return[]

def guardar_canciones(lista_canciones):
    if not os.path.exists("datos"):
        os.makedirs("datos")
    with open("datos/canciones.json","w") as archivo:
        json.dump(lista_canciones, archivo, indent=4)
