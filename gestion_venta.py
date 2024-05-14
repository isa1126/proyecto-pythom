import json


with open("producto.json", "r") as file:
    catalogo_productos = json.load(file)


def mostrar_catalogo():
    print("--- Catálogo de Productos ---")
    for categoria, productos in catalogo_productos.items():
        print(f"{categoria.capitalize()}:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}")
            print(f"Marca: {producto['marca']}")
            print(f"Precio: {producto['precio']}")
            print("--------------------------")

# Función para registrar una venta en un archivo de texto
def registrar_venta_txt(cliente, producto, cantidad):
    with open("ventas.txt", "a") as file:
        file.write(f"Cliente: {cliente}")
        file.write(f"Producto: {producto['nombre']}")
        file.write(f"Cantidad: {cantidad}")
        file.write("--------------------------")

# Función para mostrar las ventas registradas
def mostrar_ventas():
    print("--- Ventas Registradas ---")
    try:
        with open("ventas.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Aún no hay ventas registradas.")

while True:
    print("--- Menú de Ventas ---")
    print("1. Mostrar Catálogo de Productos")
    print("2. Registrar Venta")
    print("3. Mostrar Ventas Registradas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_catalogo()
    elif opcion == "2":
        mostrar_catalogo()
        cliente = input("Ingrese el nombre del cliente: ")
        categoria = input("Ingrese la categoría del producto: ").lower()
        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad vendida: "))

        # Verificar si la categoría existe en el catálogo
        if categoria not in catalogo_productos:
            print("Categoría no encontrada en el catálogo.")
            continue

        # Buscar el producto en la categoría del catálogo
        for producto in catalogo_productos[categoria]:
            if producto["nombre"].lower() == nombre_producto.lower():
                registrar_venta_txt(cliente, producto, cantidad)
                print("Venta registrada exitosamente.")
                break
        else:
            print("Producto no encontrado en la categoría seleccionada.")
    elif opcion == "3":
        mostrar_ventas()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Inténtelo de nuevo.")
