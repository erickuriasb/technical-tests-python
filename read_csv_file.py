'''
    Desafio Tecnico: Analisis de Archivo CSV

    Problema:
    Escribe un programa en Python que realice un analisis basico de un archivo CSV
    (Valores separados por comas) que contiene informacion sobre ventas.

    El archivo tiene el siguiente formato:
    producto, cantidad, precio_unitario
    Camisa, 50, 25
    Pantalon, 30, 40
    Zapatos, 20, 30

    Requisitos:
    - Lee el archivo CSV y carga los datos en una estructura adecuada en Python.
    - Calcula el total de ventas para cada producto (cantidad * precio_unitario).
    - Determina el producto mas vendido (mayor cantidad total vendida).
    - Encuentra el promedio del precio unitario de todos los productos.
    - Muestra los resultados obtenidos en un formato claro y legible.
'''
def open_file(file_name):
    try:
        with open(file_name) as file:
            data = file.readlines()
            titles = data.pop(0)
            titles = titles[:-1]
            titles = titles.split(",")
            titles = [item.strip() for item in titles]
            for row in data:
                row = row.replace("\n","")
                row = row.replace(" ", "")
                row = row.split(",")
                dataframe.append({x : y for x, y in zip(titles, row)})
    except IOError as error:
        print("No se pudo abrir el archivo.", error)


def total_ventas_producto():
    total_venta = []
    for row in dataframe:
        total_venta.append({ row["producto"]: (float(row["cantidad"]) * float(row["precio_unitario"]))})
    return total_venta


def producto_mas_vendido():
    current_max = dataframe[0]
    for row in dataframe[1:]:
        if float(row['cantidad']) > float(current_max['cantidad']):
            current_max = row
        return current_max['producto']


def promedio_precio_unitario():
    avg_price = 0
    for row in dataframe:
        avg_price += float(row['precio_unitario'])
    return round(avg_price / len(dataframe), 2)

if __name__ == "__main__":
    dataframe = []
    open_file("sales.csv")

    print("\nAnalisis de Ventas:\n")
    print("Total de ventas por producto:")
    for row in total_ventas_producto():
        for key, val in row.items():
            print(f"- {key}\t: ${val}")
    
    print(f"\nProducto mas vendido: {producto_mas_vendido()}\n")
    print(f"El Promedio del precio unitario de los productos: ${promedio_precio_unitario()}")
    
