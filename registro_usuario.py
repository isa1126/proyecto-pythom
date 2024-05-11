import json

#registro y gestion de datos
archivo_usuarios = "usuarios.json"

def cargar_usuarios():
    try:
        with open(archivo_usuarios, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_usuarios(usuarios):
    with open(archivo_usuarios, "w") as file:
        json.dump(usuarios, file, indent=4)

def crear_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    while True:
        try:
            documento= int(input("ingrese el documento del usuario: "))
            break
        except:
            print("Ingrese solo numeros")
    direccion = input("Ingrese la dirección del usuario: ")
    while True:
        try:
            telefono= int(input("ingrese el telefono del usuario: "))
            break
        except:
            print("Ingrese solo numeros")
    categoria = input("Ingrese la categoría del usuario (nuevo, regular, leal): ")
    
    usuario = {
        "nombre": nombre,
        "documento":documento,
        "direccion": direccion,
        "telefono": telefono,
        "categoria": categoria
        "servicios": [],
        "interacciones": []
    }
    
    return usuario

def agregar_usuario():
    usuarios = cargar_usuarios()
    nuevo_usuario = crear_usuario()
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)
    print("Usuario agregado correctamente.")

def mostrar_usuarios():
    usuarios = cargar_usuarios()
    for indice, usuario in enumerate(usuarios, start=1):
        print(f"Usuario {indice}:")
        print(f"Nombre: {usuario['nombre']}")
        print(f"documetos: {usuario['documento']}")
        print(f"Dirección: {usuario['direccion']}")
        print(f"Teléfono: {usuario['telefon']}")
        print(f"Categoría: {usuario['categoria']}")
        print()

def actualizar_usuario():
    usuarios = cargar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    
    mostrar_usuarios()
    
    try:
        indice_usuario = int(input("Ingrese el número de usuario que desea actualizar: ")) - 1
        usuario_actualizado = crear_usuario()
        usuarios[indice_usuario] = usuario_actualizado
        guardar_usuarios(usuarios)
        print("Usuario actualizado correctamente.")
    except (ValueError, IndexError):
        print("Número de usuario inválido.")

def eliminar_usuario():
    usuarios = cargar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    
    mostrar_usuarios()
    
    try:
        indice_usuario = int(input("Ingrese el número de usuario que desea eliminar: ")) - 1
        usuario_eliminado = usuarios.pop(indice_usuario)
        guardar_usuarios(usuarios)
        print("Usuario eliminado correctamente.")
    except (ValueError, IndexError):
        print("Número de usuario inválido.")

    Modificar el esquema de usuario
    suario = {
    "nombre": "",
    "direccion": "",
    "telefono": "",
    "categoria": "",
    "servicios_utilizados": [],
    "interacciones": []
    }

# Funciones para registrar servicios utilizados e interacciones con la empresa
def registrar_servicio(usuario, servicio):
    usuario["servicios_utilizados"].append(servicio)

def registrar_interaccion(usuario, interaccion):
    usuario["interacciones"].append(interaccion)

# Modificar las funciones cargar_usuarios() y guardar_usuarios(usuarios) para incluir los campos adicionales

# Modificar el menú para incluir opciones para ver el historial de servicios utilizados e interacciones


def menu():
    while True:
        print("\n--- Menú de Usuarios ---")
        print("1. Agregar Usuario")
        print("2. Mostrar Usuarios")
        print("3. Actualizar Usuario")
        print("4. Eliminar Usuario")
        print("5. Ver Historial de Servicios Utilizados")
        print("6. Ver Historial de Interacciones")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            actualizar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            ver_historial_servicios()
        elif opcion == "6":
            ver_historial_interacciones()
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")
       

if __name__ == "__main__":
    menu()
