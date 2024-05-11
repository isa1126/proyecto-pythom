import json


# Modificar el esquema de usuario
usuario = {
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

# Otras funciones necesarias
