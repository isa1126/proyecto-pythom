def mostrar_menu_principal():
    print("--- Menú ---")
    print("1. Modo Administrador")
    print("2. Modo Usuario")
    print("3. Salir")

def mostrar_menu_administrador():
    print("--- Menú de Administrador ---")
    print("1. Agregar Usuario")
    print("2. Mostrar Usuarios")
    print("3. Actualizar Usuario")
    print("4. Eliminar Usuario")
    print("5. Volver al Menú Principal")

def mostrar_menu_usuario():
    print("--- Menú de Usuario ---")
    print("1. Buscar prociones personalizadas")
    print("2.mostrar catalogo")
    print("3.comprar")
    print("4registrar_venta")
    print("5.Mostrar compra registradas")
    print("6. consulte por nuestro servicios ")
    print("7.volver al menu principal")


def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("***************************************")
        return opc
    except Exception:
        print("Valor inválido")
        print("***************************************")
        return -1
        
