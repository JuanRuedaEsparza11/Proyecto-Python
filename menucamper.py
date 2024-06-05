from datos import *

ruta_inscritos = "inscritos.json"

# Carga de datos
datos_inscritos = cargar_datos(ruta_inscritos)
if datos_inscritos is None:
    datos_inscritos = {}  # Manejo de caso en que la carga falle o no haya datos previos

def camper(datos_inscritos):
    print("Bienvenido Camper")
    print("Que deseas hacer el día de hoy?: ")
    print("1. Ver sus notas")
    print("2. Inscripción")
    print("3. Presentar prueba")
    print("4. Salir de camper")
    try:
        eleccion = int(input(""))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    try:
        if eleccion == 2:
            doc = input("Ingrese su número de identificación: ")
            camper = {}
            camper["nombre"] = input("Ingrese su nombre: ")
            camper["apellido"] = input("Ingrese su apellido: ")
            camper["telefono"] = input("Ingrese su teléfono: ")
            camper["direccion"] = input("Ingrese su dirección: ")
            camper["acudiente"] = input("Ingrese el nombre de su acudiente: ")
            camper["estado"] = "Inscrito"
            datos_inscritos[doc] = camper
            print("Has sido registrado exitosamente")
        elif eleccion == 3:
            doc = input("Digite su documento de identidad: ")
            if doc in datos_inscritos:
                nota1 = int(input("Ingrese su puntaje en la prueba teórica: "))
                nota2 = int(input("Ingrese su puntaje en la prueba práctica: "))
                promedio = (nota1 + nota2) / 2
                datos_inscritos[doc]["resultado pruebas"] = promedio
            else:
                print("Usuario no encontrado.")
        elif eleccion == 4:
            print("¡Hasta luego!")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Guardar datos actualizados
guardar_datos(datos_inscritos, ruta_inscritos)
            
            
            
            
            
            
            