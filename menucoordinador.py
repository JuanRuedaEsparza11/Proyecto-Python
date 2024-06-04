from datos import *

ruta_aprobados = "aprobados.json"
datos_aprobados = cargar_datos(ruta_aprobados)

ruta_inscritos = "inscritos.json"
datos_inscritos = cargar_datos(ruta_inscritos)



def coordinador(datos_inscritos, datos_aprobados):
    print("Bienvenido Coordinador") 
    print("Que deseas hacer el dia de hoy?")
    print("1. Registrar notas de campers") #aprobar campers
    print("2. Crear rutas de entrenamiento")
    print("3. Cambiar el estado de los campers")
    print("4. Ver modulo de reportes")
    print("5. Ver lista de trainers")
    print("6. Ver en que ruta estan los trainers y los campers")
    print("7. Ver los estudiantes aprobados en cada modulo")
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
            print("Tenga buen dia")

    if eleccion_coord == 3:
        doc = input("Digite el documento del estudiante: ")
        if doc in datos_aprobados["aprobados"]: 
            datos_aprobados["aprobados"][doc]["Estado"] = "aprobado"


guardar_datos(datos_aprobados, ruta_aprobados)
guardar_datos(datos_inscritos, ruta_inscritos)

        
    


























