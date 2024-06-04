import json #leer librerias json


def cargar_datos(archivo):
    with open(archivo, "r") as file:
        user = json.load(file)
        print("Se cargo correctamente!")
        return user
    
    
            #guarda datos en otro archivo
def guardar_datos(datos, archivo):
    datos = dict(datos)
    thing = json.dumps(datos, indent=4)
    file = open(archivo, "w")
    file.write(thing)
    file.close()
    