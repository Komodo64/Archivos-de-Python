ventas_precios = [15.50, 20.00, 5.75, 15.50, 30.00]

productos_vendidos = ["cafe", "torta", "galleta", "cafe", "almuerzo"]

ingresos_totales = sum(ventas_precios)

productos_unicos = set(productos_vendidos)

print(f" Ingresos totales del día: ${ingresos_totales:.2f}")
print(f" Número de productos únicos vendidos: {len(productos_unicos)}")
print(f" Productos únicos: {productos_unicos}")