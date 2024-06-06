from menucoordinador import *
from menutrainers import *
from datos import *
from menucamper import *


ruta_node = "ruta_node.json"
ruta_java = "ruta_Java.json"
ruta_net = "ruta_NetCore"
ruta_inscritos = "inscritos.json"
ruta_aprobados = "aprobados.json"
ruta_trainers = "rutas.json"

# Cargar datos

datos_inscritos = cargar_datos(ruta_inscritos)
if datos_inscritos is None:
    datos_inscritos = {}  # Manejo de caso en que la carga falle o no haya datos previos

datos_aprobados = cargar_datos(ruta_aprobados)
if datos_aprobados is None:
    datos_aprobados = {}

datos_trainers = cargar_datos(ruta_trainers)
if datos_trainers is None:
    datos_trainers = {}

try:
    inicio = open("titulo.txt", "r")
    print(inicio.read())
    cargo = int(input(""))

    if cargo == 1:
        camper(datos_inscritos)
    elif cargo == 2:
        trainer(datos_trainers)
    elif cargo == 3:
        coordinador(datos_inscritos, datos_aprobados)

except Exception as e:
    print(f"Error: {e}")

# Guardar datos actualizados
guardar_datos(datos_inscritos, ruta_inscritos)
guardar_datos(datos_aprobados, ruta_aprobados)
guardar_datos(datos_trainers, ruta_trainers)

