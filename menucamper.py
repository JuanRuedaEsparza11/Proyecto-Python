from datos import *

ruta_inscritos = "inscritos.json"               #ruta = inscritos, entons carga inscritos
datos_inscritos = cargar_datos(ruta_inscritos)  #carga ruta



def camper(datos_inscritos):
    print("Bienvenido Camper")
    print("Que deseas hacer el dia de hoy?: ")
    print("1. Ver sus notas")
    print("2. Inscripción")
    print("3. Presentar prueba")
    eleccion = int(input(""))
    
    if eleccion == 2:
        doc = input("ponga tarjeta de identidad: ")
        camper = {} 
        
        camper["nombre"] =input("ponga nombre: ")
        camper["apellido"] =input("ponga apellido: ")
        camper["telefono"] = input("ponga telefono: ")
        camper["direccion"] = input("ponga direccion: ")
        camper["acudiente"] = input("ponga su acudiente: ")
        datos_inscritos[doc] = camper
        print("Has sido registrado exitosamente")
        
    elif eleccion == 3:
        doc = input("Digite su documento de identidad: ")
        if doc in datos_inscritos:
            nota1 = int(input("Ingrese su puntaje en la prueba teorica: "))
            nota2 = int(input("Ingrese su puntaje en la prueba practica: "))
            promedio = (nota1 + nota2) / 2
            datos_inscritos[doc]["resultado pruebas"] = promedio
        else: 
            print("Chao perra")

            
            
            
            
            
            
            
            
            
            
            
            
            
            
guardar_datos(datos_inscritos, ruta_inscritos)
            
            
            
            
            
            
            