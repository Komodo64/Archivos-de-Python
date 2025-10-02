#8. Tarea: Crea una lista de diccionarios para un inventario de productos. Cada diccionario debe tener
#"nombre", "precio" y "stock". Escribe una función que busque un producto por su nombre y devuelva
#su diccionario.

# Lista de diccionarios para el inventario
inventario = [
    {"nombre": "Laptop", "precio": 800, "stock": 10},
    {"nombre": "Mouse", "precio": 20, "stock": 50},
    {"nombre": "Teclado", "precio": 35, "stock": 30},
    {"nombre": "Monitor", "precio": 150, "stock": 15}
]

# Función para buscar producto por nombre
def buscar_producto(nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

# Ejemplo de uso
nombre_buscar = input("Digite el nombre del producto a buscar: ")
resultado = buscar_producto(nombre_buscar)

if resultado:
    print("Producto encontrado:", resultado)
else:
    print("Producto no encontrado en el inventario.")

