import json

nombre_archivo = "usuarios.json"


def cargar_usuarios():
    try:
        with open(nombre_archivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_usuarios(usuarios):
    with open(nombre_archivo, "w") as file:
        json.dump(usuarios, file, indent=4)

# Función para buscar un usuario por su documento
def buscar_por_documento(documento):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if str(usuario.get("documento")) == str(documento):
            return usuario
    return None

# Función para personalizar servicios según la categoría del usuario
def personalizar_servicios(usuario):
    categoria = usuario.get("categoria")
    if categoria == "Nuevo cliente":
        print("¡Bienvenido! Le recomendamos nuestro paquete de bienvenida.")
    elif categoria == "Cliente regular":
        print("Como cliente regular, puede disfrutar de descuentos exclusivos en nuestros servicios.")
    elif categoria == "Cliente leal":
        print("Gracias por su lealtad. Como cliente leal, le ofrecemos acceso anticipado a nuestras promociones.")
    else:
        print("No se ha especificado una categoría válida para este usuario.")


def menu():
    while True:
        print("--- Menú ---")
        print("Aqui puedes ver tus ofertas personalizadas")
    
        print("1. Buscar Usuario por Documento")
        print("2. Salir")
    
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            documento = input("Ingrese el documento del usuario: ")
            usuario = buscar_por_documento(documento)
            if usuario:
                personalizar_servicios(usuario)
            else:
                print("Usuario no encontrado.")
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")


menu()

