import json
from datos import *
from crud_servicios import *

with open("usuario.json","r") as file:
    usuarios=json.load(file)
    for user in usuarios:
        print("Nombre del usuario:", usuarios["nombre"], "Documento del usuario:", usuarios["documento"], "Direccion del usuario:", usuarios["direccion"], "Ingrese el telefono", usuarios["telefono"])
        


RUTA_PRODUCTO = "servicios.json"

dato_servicio = cargar_datos(RUTA_PRODUCTO)

dato_servicio = eliminar_servicios(dato_servicio)

guardar_datos(dato_servicio, RUTA_PRODUCTO)
