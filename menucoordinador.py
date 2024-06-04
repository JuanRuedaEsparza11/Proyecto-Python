from datos import *

ruta_inscritos = "inscritos.json"
datos_inscritos = cargar_datos(ruta_inscritos)

ruta_aprobados = "aprobados.json"
datos_aprobados = cargar_datos(ruta_aprobados)

def coordinador(datos_inscritos, datos_aprobados):
    print("Bienvenido Coordinador") 
    print("Que deseas hacer el dia de hoy?")
    print("1. Registrar notas de campers") #aprobar campers
    print("2. Crear rutas de entrenamiento")
    print("3. Ver modula de reportes")
    print("4. Cambiar el estado de los campers")
    print("5. Ver lista de trainers")
    print("6. Ver en que ruta estan los trainers y los campers")
    print("7. Ver los estudiantes aprobados en cada modulo")
    eleccion_coord = int(input(""))
    
    if eleccion_coord == 1:
        doc = input("Digite su documento: ")
        if doc in datos_inscritos:
            estudiante = datos_inscritos[doc]
            if datos_inscritos[doc]["resultado pruebas"] >= 60: 
                datos_aprobados["aprobados"][doc] = estudiante
                print("Has sido aprobado")
                print("Disfruta tu experiencia en Campus-Lands")
            
        else: 
            print("Chao perra")

        
    


























