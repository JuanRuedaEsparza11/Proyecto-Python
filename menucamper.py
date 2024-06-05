from datos import *

ruta_inscritos = "inscritos.json"
datos_inscritos = cargar_datos(ruta_inscritos)
if datos_inscritos is None:
    datos_inscritos = {}  # Manejo de caso en que la carga falle o no haya datos previos

def camper(datos_inscritos):
    try:
        print("Bienvenido Camper")
        print("Que deseas hacer el día de hoy?: ")
        print("1. Inscripción")
        print("2. Presentar prueba")
        print("3. Presentar prueba de modulo")
        print("4. Salir de camper")
        eleccion = int(input(""))

        if eleccion == 1:
            doc = input("Ingrese su número de identificación: ")
            camper_data = {}
            camper_data["nombre"] = input("Ingrese su nombre: ")
            camper_data["apellido"] = input("Ingrese su apellido: ")
            camper_data["telefono"] = input("Ingrese su teléfono: ")
            camper_data["direccion"] = input("Ingrese su dirección: ")
            camper_data["acudiente"] = input("Ingrese el nombre de su acudiente: ")
            camper_data["estado"] = "Inscrito"
            camper_data["prueba_modulo"] = 
            datos_inscritos[doc] = camper_data
            print("Has sido registrado exitosamente")

        elif eleccion == 2:
            doc = input("Digite su documento de identidad: ")
            if doc in datos_inscritos:
                nota1 = int(input("Ingrese su puntaje en la prueba teórica: "))
                nota2 = int(input("Ingrese su puntaje en la prueba práctica: "))
                promedio = (nota1 + nota2) / 2
                datos_inscritos[doc]["resultado_pruebas"] = promedio
            else:
                print("Usuario no encontrado.")
        elif eleccion == 3:
            doc = input("Digite su documento de identidad: ")
            if doc in datos_inscritos:
                nota_modulo = int(input("Ingrese su calificacion en la prueba del modulo: "))
                datos_inscritos[doc]["resultado_pruebas_modulo"] = nota_modulo
            else:
                print("Usuario no encontrado.")
        elif eleccion == 4:
            print("¡Hasta luego!")
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

    except ValueError:
        print("Por favor, ingrese un número válido.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    # Guardar datos actualizados
    guardar_datos(datos_inscritos, ruta_inscritos)

camper(datos_inscritos)
            
            
            
            
            
            