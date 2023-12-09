'''
    Requisitos:
    - Utiliza un diccionario para almacenar los contactos, donde el nombre del contacto es la clave y el número de teléfono es el valor.
    - El programa debe permitir al usuario ingresar comandos para realizar las operaciones mencionadas anteriormente.
    - Debe manejar casos en los que el usuario ingrese un nombre que no existe en los contactos.
    - El programa debe continuar ejecutándose hasta que el usuario elija salir explícitamente.
'''

def add_name():
    name = input("Ingrese el nombre del contacto: ")
    phone = input("Ingrese el numero de telefono: ")
    address_book.update({name : phone})
    return


def print_menu():
    print("\nBienvenido al sistema de Gestion de Contactos.\n\n")
    print("Por favor, selecciona una opcion:\n1. Agregar un nuevo contacto\n2. Buscar un contacto\n3. Mostrar todos los contactos.\n4. Salir\n\n")
    return


def get_name():
    name = input("\nIngrese el nombre del contacto a buscar: ")
    if address_book.get(name) == None :
        print(f"\nContacto \"{name}\" no encontrado.\n\n")
    else:    
        print(f"\nEl numero de contacto de {name} es: {address_book.get(name)}\n\n")
    return


def print_agenda():
    print("\nLista de Contactos: \n")
    for key in address_book.keys():
        print(f"{key}\t: {address_book[key]}")
    print("\n\n")
    return


if __name__ == "__main__":
    global address_book
    address_book = {}
    while True:
        print_menu()
        option = int(input("Ingrese el numero de la opcion deseada: "))
        if option == 1:
            add_name()
        elif option == 2:
            get_name()
        elif option == 3:
            print_agenda()
        elif option == 4:
            print("Adios!")
            break
        else:
            print("La opcion que ingreso no esta en el menu. Intente de nuevo")

