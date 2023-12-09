'''
Desafio Tecnico: Gestion de Almacenamiento de Productos

Problema:
Escribe un programa en Python que simule la gestion de un almacen
de productos. El programa debe permitir agregar, buscar, actualizar
y eliminar productos del almacen.

Requisitos:
- Utiliza un diccionario para almacenar la informacion de los productos,
donde el codigo del producto es la clave y los detalles de producto son
los valores (nombre, precio, cantidad, etc.).
- El programa debe ofrecer las siguientes operaciones:
    1. Agregar un nuevo producto: Solicitar al usuario ingresar el codigo,
    nombre y cantidad del nuevo producto y agregarlo al almacen.
    2. Buscar un producto por codigo: Mostrar los detalles de un producto
    especifico cuando se ingresa su codigo.
    3. Actualizar la informacion de un producto: Permitir al usuario actualizar
    el nombre, precio o cantidad de un producto existente utilizando su codigo.
    4. Eliminar un producto: Elimiar un producto del almacen usando su codigo.
    5. Mostrar todos los productos almacenados: Mostrar una lista con todos los
    productos y sus detalles almacenados en el almacen
'''
def imprimir_menu():
    print("\nGestion de Almacenamiento de Productos\n\n")
    print("1. Agregar un nuevo producto\n2. Buscar un producto por codigo")
    print("3. Actualizar informacion de un producto\n4. Eliminar un producto")
    print("5. Mostrar todos los productos almacenados\n6. Salir\n\n")
    return


def inventario_vacio():
    if len(almacen_productos) == 0:
        return True
    return False


def agregar_producto():
    codigo = input("Ingrese el codigo del nuevo producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: $")
    cantidad = input("Ingrese la cantidad del producto: ")
    almacen_productos.append({
        'codigo': codigo,
        'nombre': nombre,
        'precio': float(precio),
        'cantidad': int(cantidad)
    })
    return


def mostrar_productos():
    print("\nLista de Productos Almacenados: \n")
    if inventario_vacio():
        print("No hay productos registardos hasta ahora.\n\n")
    else:
        for row in almacen_productos:
            print(f"- Codigo: {row['codigo']}, Nombre: {row['nombre']}, Precio: ${round(row['precio'],2)}, Cantidad: {row['cantidad']}")
    return


def buscar_producto():
    if inventario_vacio():
        print("No hay productos registardos hasta ahora.\n\n")
    else:
        codigo = input("Ingrese el codigo del producto para buscar: ")
        for row in almacen_productos:
            if row['codigo'] == codigo:
                print("Detalles del producto:")
                print(f"- Codigo: {row['codigo']}\n- Nombre: {row['nombre']}\n- Precio: ${row['precio']}\n- Cantidad: {row['cantidad']}\n\n")
                return
        print("No se encontro un producto con el codigo que ingreso.")
    return

def actualizar_producto():
    if inventario_vacio():
        print("No hay productos registardos hasta ahora.\n\n")
    else:
        codigo = input("Ingrese el codigo del producto a actualizar: ")
        count = 0
        for row in almacen_productos:
            if row['codigo'] == codigo:
                info = input("Que informacion desea actualizar? (nombre/precio/cantidad): ")
                value = input(f"Ingrese el nuevo valor de {info}: ")
                if info == 'precio':
                    row[info] = float(value)
                else:
                    row[info] = value
                almacen_productos.pop(count)
                almacen_productos.insert(count, row)
                print("Informacion actualizada correctamente. \n")
                return
            count += 1
        print("No se encontro un registro con ese codigo.")
        return

def eliminar_producto():
    if inventario_vacio():
        print("No se encontro un registro con ese codigo.")
    else:
        codigo = input("Ingrese el codigo del producto que desea eliminar: ")
        count = 0
        for row in almacen_productos:
            if row['codigo'] == codigo:
                almacen_productos.pop(count)
                print("Producto eliminado exitosamente.\n\n")
                return
            else:
                count =+ 1
        print("No se encontro un registro con ese codigo.")
    return


if __name__ == "__main__":
    almacen_productos = []
    while True:
        imprimir_menu()
        opcion = input("Ingrese el numero de opnion deseada: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            mostrar_productos()
        elif opcion == "6":
            print("Gracias por utilizar el Gestor de Almacenamiento de Productos!")
            break
        else:
            print("La opcion que ingreso no esta en el Menu, intente nuevamente.")
