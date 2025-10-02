respuestas = [5, 4, 3, 5, 5, 2, 4, 5, 1, 5]

contador_max_satisfaccion = 0

# Recorremos todas las respuestas
for r in respuestas:
    if r == 5:
        contador_max_satisfaccion += 1

# Convertimos la lista en conjunto para obtener respuestas únicas
respuestas_unicas = set(respuestas)

print("Total de personas 'muy satisfechas' (respuesta 5):", contador_max_satisfaccion)
print("Opciones únicas de respuesta marcadas:", respuestas_unicas)
