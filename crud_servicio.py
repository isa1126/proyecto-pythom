import json

def cargar_servicios():
    try:
        with open("servicios.json", "r") as file:
            return json.load(file)
    except FileExistsError:
        return[]
    
def guardar_servicios(servicios):
    with open("servicios.json", "w") as file:
        json.dump(servicios, file, indent=4)

def agregar_servicio(nuevo_servicio):
    servicios = cargar_servicios
    servicios.append(nuevo_servicio)
    guardar_servicios(servicios)

def obtener_servocio(nombre_servicio, datos_actualizados):
    servicios= cargar_servicios()
    for servicio in servicios:
        if servicio["nombre"] == nombre_servicio:
            servicio.update(datos_actualizados)
            guardar_servicios(servicios)
    return None

def actualizar_servicios(nombre_servicios, datos_actualizados):
    servicios= cargar_servicios()
    for servicio in servicios:
        if servicio["nombre"]== nombre_servicios:
            servicio.update(datos_actualizados)
            guardar_servicios(servicios)
        return True
    return False  

def eliminar_servicios(nombre_servicios):
    servicios= cargar_servicios()
    for servicio in servicios:
        if servicio["nombre"]== nombre_servicios:
            servicio.remove(servicio)
            guardar_servicios(servicios)
        return True
    return False  