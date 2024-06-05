import json  # Leer librerías JSON


def cargar_datos(archivo):
    try:
        with open(archivo, "r") as file:
            user = json.load(file)
            print("Se cargaron los datos correctamente!")
            return user
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return None


# Guardar datos en otro archivo
def guardar_datos(datos, archivo):
    try:
        datos = dict(datos)
        thing = json.dumps(datos, indent=4)
        with open(archivo, "w") as file:
            file.write(thing)
        print("Se guardaron los datos correctamente!")
    except Exception as e:
        print(f"Error al guardar datos: {e}")
    #datos_node["NodeJs"]["trainers"]["111"]["M1"]["campers"] = datos["aprobados"]["1099739701"]