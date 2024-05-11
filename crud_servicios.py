def servicio_agregar(datos_servicio):
    datos_servicio = dict(datos_servicio)
    servicio ={}
    servicio["numero_servicio"]= int(input("ingrese codigo: "))
    servicio["nombre"]= input("ingrese nombre: ")
    servicio["precio"]= int(input("ingrese precio: "))
    datos_servicio["servicios"].append(servicio)
    return datos_servicio


def eliminar_servicios(datos_servicio):
    numero_servicio=int(input("Ingrese el numero del servicio que desea eliminar: "))
    lista = datos_servicio.get("servicios")
    lista = list(lista)
    for i in lista:
        if i.get("numero_servicio") == numero_servicio:
            lista.remove(i)
    datos_servicio["servicios"] = lista
    return datos_servicio
