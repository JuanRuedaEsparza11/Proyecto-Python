from datos import *

ruta_aprobados = "aprobados.json"

# Cargar datos de aprobados
datos_aprobados = cargar_datos(ruta_aprobados)
if datos_aprobados is None:
    datos_aprobados = {}  # Manejo de caso en que la carga falle o no haya datos previos

def trainer(datos_trainers):
    try:
        print("Bienvenido Trainer")
        print("Que deseas hacer el día de hoy?")
        print("1. Inspeccionar cursos")
        print("2. Inspeccionar notas de algún estudiante")
        print("3. Asignar notas a campers")
        elecc_train = input("")

        if elecc_train == 3:
            doc = input()

        # Agrega aquí tu lógica para las opciones del trainer
        
    except Exception as e:
        print(f"Error: {e}")

# Guardar datos actualizados
guardar_datos(datos_aprobados, ruta_aprobados)















