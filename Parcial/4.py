# Inicializamos el diccionario con colores y sus votos en 0
votos = {
    "rojo": 0,
    "azul": 0,
    "verde": 0,
    "amarillo": 0
}

# Mostrar opciones disponibles
print("Opciones de colores para votar:")
for color in votos:
    print(f"- {color}")

# Pedir al usuario un voto
opcion = input("Elige tu color favorito: ").lower()

# Verificar si la opción está en el diccionario
if opcion in votos:
    votos[opcion] += 1  # Actualizamos el valor
    print(f"✅ Tu voto por '{opcion}' ha sido registrado.")
else:
    print("❌ Opción inválida, ese color no está en la lista.")

# Mostrar resultados finales
print("\nResultados de la votación:")
for color, cantidad in votos.items():
    print(f"{color}: {cantidad} votos")
