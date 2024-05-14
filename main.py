from menu import *
from usuario import *
from per_servicio import *
from gestion_venta import*

RUTA_BASE_DE_DATOS = "usuarios.json"
datos = cargar_usuarios(RUTA_BASE_DE_DATOS)
tiempo_en_claro= cargar_usuarios(RUTA_BASE_DE_DATOS)

def main():
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Seleccione una opción: ")

        if opcion_principal == "1": 
            while True:
                mostrar_menu_administrador()
                opcion_administrador = input("Seleccione una opción: ")
                if opcion_administrador == "1":
                
                    dato=crear_usuario()
                    dato= obtener_tiempo_en_claro()
                    dato= asignar_categoria_por_tiempo(tiempo_en_claro)
                    pass
                elif opcion_administrador == "2":
                    mostrar_usuarios()
                    pass
                elif opcion_administrador == "3":
                    actualizar_usuario()
                    pass
                elif opcion_administrador == "4":
                    eliminar_usuario()
                    pass
                elif opcion_administrador == "5":
                    print("salir")
                    break 
                else:
                    print("Opción no válida.")

        elif opcion_principal == "2":  # Modo Usuario
            while True:
                mostrar_menu_usuario()
                opcion_usuario = input("Seleccione una opción: ")
                if opcion_usuario == "1":
                    buscar_por_documento(documento)
                elif opcion_usuario == "2":
                    personalizar_servicios(usuario)
                elif opcion_usuario == "3":
                    mostrar_catalogo()
                elif opcion_usuario == "4": 
                     registrar_venta_txt(cliente, producto, cantidad)
                elif opcion_usuario == "5": 
                    mostrar_ventas()
                elif opcion_usuario == "6":
                    print("salir")
                    break 
                else:
                    print("Opción no válida.")
menu()