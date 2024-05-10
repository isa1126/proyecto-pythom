import json

def cargar_datos(servicios):
    datos = {}
    with open(servicios,"r") as file:
        servicios=json.load(file)
    return datos
        
        

def guardar_datos(datos, servicio):
    datos= dict(datos)
    
    dato =json.dumps(datos, indent=4)
    file=open(servicio,"w")
    file.write(dato)
    file.close()