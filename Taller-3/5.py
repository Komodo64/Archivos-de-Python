#5. Tarea: Crea un diccionario que funcione como un pequeño traductor de inglés a español. Pide al
#usuario una palabra en inglés y muestra su traducción si existe en el diccionario.

# Diccionario traductor
traductor = {
    "cat": "gato",
    "dog": "perro",
    "house": "casa",
    "car": "coche",
    "book": "libro"
}

# Pedir palabra en inglés
palabra = input("Digite una palabra en inglés: ").lower()

# Buscar traducción
if palabra in traductor:
    print("La traducción es:", traductor[palabra])
else:
    print("La palabra no está en el diccionario.")

