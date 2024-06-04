from menucoordinador import *
from datos import *
from menucamper import *
ruta_inscritos = "inscritos.json"
datos_inscritos = cargar_datos(ruta_inscritos)

ruta_aprobados = "aprobados.json"
datos_aprobados = cargar_datos(ruta_aprobados)













inicio = open("titulo.txt", "r")
print(inicio.read())
cargo = int(input(""))

if cargo == 1:
    camper(datos_inscritos)
elif cargo == 3:
    coordinador(datos_inscritos, datos_aprobados)

















guardar_datos(datos_inscritos, ruta_inscritos)


