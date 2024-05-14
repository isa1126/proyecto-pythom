import json


archivo_usuarios = "usuarios.json"

def cargar_usuarios():
    try:
        with open(archivo_usuarios, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_usuarios(usuarios):
    with open(archivo_usuarios, "w") as file:
        json.dumps(usuarios, file, indent=4)

#registro usuario

def obtener_tiempo_en_claro():
    while True:
        try:
            tiempo = float(input("Ingrese la cantidad de meses que lleva en Claro: "))
            if tiempo >= 0:
                return tiempo / 12  # Convertir meses a años
            else:
                print("Ingrese un número positivo.")
        except ValueError:
            print("Ingrese un número válido.")

def asignar_categoria_por_tiempo(tiempo_en_claro):
    if tiempo_en_claro < 8/12:  # Menos de 8 meses (convertidos a años)
        return "Nuevo cliente"
    elif 8/12 <= tiempo_en_claro < 5:  # Entre 8 meses y menos de 5 años
        return "Cliente regular"
    else:  # 5 años o más
        return "Cliente leal"

def crear_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    while True:
        documento = input("Ingrese el documento del usuario: ")
        try:
            documento = int(documento)
            break  # Si la conversión es exitosa, salimos del bucle
        except ValueError:
            print("Ingrese solo números")

    direccion = input("Ingrese la dirección del usuario: ")
    while True:
        try:
            telefono = int(input("Ingrese el teléfono del usuario: "))
            break
        except ValueError:
            print("Ingrese solo números")

    tiempo_en_claro = obtener_tiempo_en_claro()
    categoria = asignar_categoria_por_tiempo(tiempo_en_claro)

    usuario = {
        "nombre": nombre,
        "documento": documento,
        "direccion": direccion,
        "telefono": telefono,
        "categoria": categoria,
        "servicio_utilizado": [],
        "interaccion": []
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
        print(f"Documento: {usuario['documento']}")
        print(f"Dirección: {usuario['direccion']}")
        print(f"Teléfono: {usuario['telefono']}")
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
        if 0 <= indice_usuario < len(usuarios):
            usuario_actualizado = crear_usuario()
            usuarios[indice_usuario] = usuario_actualizado
            guardar_usuarios(usuarios)
            print("Usuario actualizado correctamente.")
        else:
            print("Número de usuario inválido.")
    except ValueError:
        print("Número de usuario inválido.")

def eliminar_usuario():
    usuarios = cargar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    
    mostrar_usuarios()
    
    try:
        indice_usuario = int(input("Ingrese el número de usuario que desea eliminar: ")) - 1
        if 0 <= indice_usuario < len(usuarios):
            usuario_eliminado = usuarios.pop(indice_usuario)
            guardar_usuarios(usuarios)
            print("Usuario eliminado correctamente.")
        else:
            print("Número de usuario inválido.")
    except ValueError:
        print("Número de usuario inválido.")

def menu():
    while True:
        print("--- Menú de Usuarios ---")
        print("1. Agregar Usuario")
        print("2. Mostrar Usuarios")
        print("3. Actualizar Usuario")
        print("4. Eliminar Usuario")
        print("5. Salir")
        
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
            print("salir")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")
       
menu()

 
