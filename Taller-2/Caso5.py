# Datos iniciales
calificaciones = [3.5, 4.0, 5.0, 2.5, 3.5, 4.0, 4.8]

# 1. Calcular el promedio
promedio = sum(calificaciones) / len(calificaciones)

# 2. Crear conjunto de notas únicas
notas_unicas = set(calificaciones)

# 3. Mostrar resultados
print(f"Promedio de calificaciones: {promedio:.2f}")
print("Notas únicas obtenidas:", notas_unicas)
