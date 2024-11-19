import sys
sys.stdout.reconfigure(encoding='utf-8')



# Diccionarios para almacenar productos y ventas
productos = {}  # Contiene los productos con su nombre, categoría y precio
ventas = {}  # Registra las ventas realizadas por cada cliente

# Funciones del sistema

def registrar_producto(productos, nombre, categoria, precio):
    """
    Registra un producto con su nombre, categoría y precio.
    """
    productos[nombre] = {'categoria': categoria, 'precio': precio}
    print(f"Producto '{nombre}' registrado.")

def registrar_venta(ventas, cliente, producto, cantidad):
    """
    Registra una venta realizada por un cliente, asociando el producto y la cantidad vendida.
    """
    if cliente not in ventas:
        ventas[cliente] = []
    ventas[cliente].append((producto, cantidad))
    print(f"Venta registrada: {cliente} compró {cantidad} unidades de '{producto}'.")

def calcular_total_cliente(ventas, cliente, productos):
    """
    Calcula el total gastado por un cliente en sus compras.
    """
    total = 0
    if cliente in ventas:
        for producto, cantidad in ventas[cliente]:
            total += productos[producto]['precio'] * cantidad
    return total

def mostrar_estadisticas(ventas, productos):
    """
    Muestra estadísticas sobre las ventas y los productos más vendidos.
    """
    print("--- Estadísticas ---")
    
    # Calcular las ventas totales de cada producto
    ventas_totales = {producto: 0 for producto in productos}
    for cliente, lista_ventas in ventas.items():
        for producto, cantidad in lista_ventas:
            ventas_totales[producto] += cantidad
    
    # Mostrar las ventas totales por producto
    for producto, total in ventas_totales.items():
        print(f"Producto '{producto}': {total} unidades vendidas.")
    
    # Mostrar el cliente con mayores compras
    cliente_mayores_compras = max(ventas, key=lambda cliente: calcular_total_cliente(ventas, cliente, productos))
    total_compras_cliente = calcular_total_cliente(ventas, cliente_mayores_compras, productos)
    print(f"El cliente con mayores compras es {cliente_mayores_compras} con un total de {total_compras_cliente}.")

    # Mostrar el producto más vendido
    producto_mas_vendido = max(ventas_totales, key=ventas_totales.get)
    print(f"El producto más vendido es '{producto_mas_vendido}'.")

# Programa principal: ejemplo de uso
registrar_producto(productos, "Laptop", "Electrónica", 1200)
registrar_producto(productos, "Smartphone", "Electrónica", 800)
registrar_producto(productos, "Silla Gamer", "Mobiliario", 300)

registrar_venta(ventas, "Juan Pérez", "Laptop", 1)
registrar_venta(ventas, "María López", "Smartphone", 2)
registrar_venta(ventas, "Carlos García", "Silla Gamer", 3)
registrar_venta(ventas, "Juan Pérez", "Smartphone", 1)
registrar_venta(ventas, "Carlos García", "Laptop", 1)

# Mostrar estadísticas
mostrar_estadisticas(ventas, productos)