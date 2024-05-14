
import json

def registrar_servicio_utilizado(indice_usuario, servicio):
    usuarios = cargar_usuarios()
    if 0 <= indice_usuario < len(usuarios):
        if "servicios_utilizados" not in usuarios[indice_usuario]:
            usuarios[indice_usuario]["servicios_utilizados"] = []  
        usuarios[indice_usuario]["servicios_utilizados"].append(servicio)
        guardar_usuarios(usuarios)
        print("Servicio registrado correctamente para el usuario.")
    else:
        print("Número de usuario inválido.")

# Función para registrar una interacción del usuario con la empresa
def registrar_interaccion_usuario(indice_usuario, interaccion):
    usuarios = cargar_usuarios()
    if 0 <= indice_usuario < len(usuarios):
        if "interacciones" not in usuarios[indice_usuario]:
            usuarios[indice_usuario]["interacciones"] = []  
        usuarios[indice_usuario]["interacciones"].append(interaccion)
        guardar_usuarios(usuarios)
        print("Interacción registrada correctamente para el usuario.")
    else:
        print("Número de usuario inválido.")

def menu():
    while True:
        print("--- Menú de Usuarios ---")
        print("5. Registrar Servicio Utilizado por Usuario")
        print("6. Registrar Interacción del Usuario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "5":
            indice_usuario = int(input("Ingrese el número de usuario al que desea registrar el servicio: ")) - 1
            servicio = input("Ingrese el servicio utilizado por el usuario: ")
            registrar_servicio_utilizado(indice_usuario, servicio)
        elif opcion == "6":
            indice_usuario = int(input("Ingrese el número de usuario al que desea registrar la interacción: ")) - 1
            interaccion = input("Ingrese la interacción del usuario con la empresa: ")
            registrar_interaccion_usuario(indice_usuario, interaccion)
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")


menu()
