#3. Tarea: Almacena las coordenadas (latitud, longitud) de una ciudad en una tupla. Luego, utiliza el
#desempaquetado de tuplas para asignar la latitud y la longitud a dos variables separadas e imprímelas

# Pedir coordenadas al usuario
latitud = float(input("Digite la latitud: "))
longitud = float(input("Digite la longitud: "))

# Guardar en una tupla
coordenadas = (latitud, longitud)

# Desempaquetado de la tupla
lat, lon = coordenadas

# Imprimir resultados
print("\nCoordenadas almacenadas:")
print("Latitud:", lat)
print("Longitud:", lon)
