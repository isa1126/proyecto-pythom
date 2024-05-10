from datos import *
from crud_servicios import *

RUTA_PRODUCTO = "servicios.json"

dato_servicio = cargar_datos(RUTA_PRODUCTO)

dato_servicio = servicio_agregar(dato_servicio)



guardar_datos(dato_servicio, RUTA_PRODUCTO)