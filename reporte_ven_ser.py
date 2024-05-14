import json


def cargar_productos():
    try:
        with open("productos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def guardar_servicio(servicio):
    with open("ventas.json", "w") as file:
        json.dump(servicio, file, indent=4)

def guardar_productos(productos):
    with open("productos.json", "w") as file:
        json.dump(productos, file, indent=4)


def registrar_producto(nombre, tipo, precio):
    productos = cargar_productos()
    productos.append({
        "nombre": nombre,
        "tipo": tipo,
        "precio": precio
    })
    guardar_productos(productos)
    print("Producto registrado exitosamente.")


def registrar_venta(cliente, producto, cantidad):
    ventas = cargar_ventas()
    fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ventas.append({
        "cliente": cliente,
        "producto": producto,
        "cantidad": cantidad,
        "fecha_venta": fecha_venta
    })
    guardar_ventas(ventas)
    print("Venta registrada exitosamente.")


def cargar_ventas():
    try:
        with open("ventas.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []






