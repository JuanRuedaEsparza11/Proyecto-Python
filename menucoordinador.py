from datos import *
from principal import *
# Cargar datos

ruta_java = "ruta_Java.json"
datos_java = cargar_datos(ruta_java)

ruta_net = "ruta_NetCore.json"
datos_net = cargar_datos(ruta_net)

ruta_node = "ruta_node.json"
datos_node = ruta_node

ruta_trainers = "rutas.json"
datos_trainers = cargar_datos(ruta_trainers)

ruta_aprobados = "aprobados.json"
datos_aprobados = cargar_datos(ruta_aprobados)

ruta_inscritos = "inscritos.json"
datos_inscritos = cargar_datos(ruta_inscritos)

def coordinador(datos_inscritos, datos_aprobados):
    try:
        print("Bienvenido Coordinador") 
        print("Que deseas hacer el día de hoy?")
        print("1. Aprobar Campers")
        print("2. Crear rutas de entrenamiento")
        print("3. Cambiar el estado de los campers")
        print("4. Ver modulo de reportes")
        print("5. Ver lista de trainers")
        print("6. Ver en que ruta están los trainers y los campers")
        print("7. Ver los estudiantes aprobados en cada módulo")
        eleccion_coord = int(input(""))

        if eleccion_coord == 1:
            doc = input("Digite el documento del estudiante: ")
            if doc in datos_inscritos:
                estudiante = datos_inscritos[doc]
                if datos_inscritos[doc]["resultado pruebas"] >= 60: 
                    datos_aprobados["aprobados"][doc] = estudiante
                    print("Has sido aprobado")
                    print("Disfruta tu experiencia en Campus-Lands")
                    print(ruta_aprobados)
                else: 
                    print("Usted no ha sido aprobado")
                    print("Tenga buen día")
            else:
                print("Usuario no encontrado.")

        if eleccion_coord == 2:
            doc = input("Ingrese el documento de identidad del estudiante")
            doc_trainer = input("Ingrese el documento de identidad del trainer")
            if doc in datos_aprobados["aprobados"]:
                estudiante = datos_aprobados["aprobados"][doc]
                print("1. Java")
                print("2. Node.js")
                print("3. NetCore")
                opc = int(input("A que ruta deseas agregar el estudiante?"))
                ruta = None
                
                if opc == 1:
                    ruta = "Java"
                    datos_java["Java"]["trainers"][doc_trainer]["M1"]["campers"] = estudiante
                elif opc == 2:
                    ruta = "Node.js"
                    datos_node["Node.js"]["trainers"][doc_trainer]["M1"]["campers"] = estudiante
                elif opc == 3:
                    ruta = "NetCore"
                    datos_net["NetCore"]["trainers"][doc_trainer]["M1"]["campers"] = estudiante
                else:
                    print("No existe esa ruta todavía...")
                    return

        if eleccion_coord == 3:
            doc = input("Digite el documento del estudiante: ")
            if doc in datos_aprobados["aprobados"]: 
                datos_aprobados["aprobados"][doc]["Estado"] = "aprobado"
                print("El estado del estudiante ha sido registrado")

        if eleccion_coord == 5:
            for id_tr, name_tr in datos_trainers["trainers"].items():
                print(f"Id: {id_tr}, Name:{name_tr}")

    except Exception as e:
        print(f"Error: {e}")

# Guardar datos actualizados
guardar_datos(datos_inscritos, ruta_inscritos)
guardar_datos(datos_aprobados, ruta_aprobados)
guardar_datos(datos_trainers, ruta_trainers)

        
    


























