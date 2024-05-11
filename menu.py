import json


def restro_usuario():
    nombre= input("Ingrese el nombre del usuario: ")
    
    while True:
        try:
            documento= int(input("ingrese el documento del usuario: "))
            break
        except:
            print("Ingrese solo numeros")
    direcion=input("Ingrese el direccion: ")
    while True:
        try:
            telefono= int(input("ingrese el telefono del usuario: "))
            break
        except:
            print("Ingrese solo numeros")
    categoria= input("Ingrese la categoria del usuario nuevo, regular,leal: ")
    

def cargar_usuarios():
    try:
        with open("usuarios.json","r") as file:
            return json.load(file)
    except FileExistsError:
        return ()
    
def guardar_usuarios(usuario):
    with open("usuario.json", "w") as file:
        json.dump(usuario, file, indent=4)
        
def agregar_usuario(nuevo_usuario):
    usuarios = cargar_usuarios()
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)
    
def numero_usuario(numero_usuario):
    usuario= cargar_usuarios()
    for usuarios in usuario:
        if usuarios["numero"]== numero_usuario:
            return usuario
    return None
    
def actualizar_usuario(numero_usuario, usuario_actializado):
    usuarios =cargar_usuarios()
    for usuario in usuarios:
        if usuario["numero"]== numero_usuario:
            usuario.update(usuario_actializado)
            guardar_usuarios(usuario)
            return True
    return False

def eliminar_usuario(numero_usuario):
    usuarios= cargar_usuarios()
    usuario_actualizado=[usuario for usuario in usuario if usuario["identificardor"] != numero_usuario]
    if len(usuario_actualizado)!= len (usuarios):
        guardar_usuarios(usuario_actualizado)
        return True
    return False
        
        
restro_usuario()