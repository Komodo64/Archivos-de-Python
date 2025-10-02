#14. Tarea: Tienes tres estructuras de datos: un diccionario con información de productos (ID a
#nombre), un diccionario con precios (ID a precio) y una lista de tuplas que representa las ventas del
#día (ID de producto, cantidad vendida). Calcula el ingreso total del día.

# Diccionario de productos
productos = {
    101: "Leche",
    102: "Pan",
    103: "Huevos"
}

# Diccionario de precios
precios = {
    101: 4500,
    102: 2500,
    103: 8000
}

# Lista de ventas (ID producto, cantidad vendida)
ventas_del_dia = [
    (101, 5),  # 5 Leche
    (102, 10), # 10 Pan
    (101, 3),  # 3 Leche
    (103, 2)   # 2 Huevos
]

# Calcular el ingreso total
ingreso_total = 0
for id_producto, cantidad in ventas_del_dia:
    ingreso_total += precios[id_producto] * cantidad

# Mostrar resultado
print("El ingreso total del día es:", ingreso_total)

