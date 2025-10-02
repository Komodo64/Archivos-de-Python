#13. Tarea: Tienes un diccionario que contiene información sobre un libro, incluyendo una lista de
#autores (que son diccionarios). Tu tarea es crear una lista que contenga únicamente los nombres de
#todos los autores del libro.

# Diccionario del libro
libro = {
    "titulo": "Python para Todos",
    "año": 2024,
    "autores": [
        {"nombre": "Raúl", "nacionalidad": "Española"},
        {"nombre": "Laura", "nacionalidad": "Mexicana"}
    ],
    "editorial": "Ediciones Código"
}

# Crear lista con solo los nombres de los autores
nombres_autores = [autor["nombre"] for autor in libro["autores"]]

# Mostrar resultado
print("Autores del libro:", nombres_autores)
