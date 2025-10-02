#2. Tarea: Crea un diccionario para almacenar el perfil de un usuario con las claves "nombre" y "edad".
#Luego, actualiza la edad del usuario y añade una nueva clave "ciudad" con su valor correspondiente.
#Muestra el diccionario final

# Crear diccionario con datos iniciales
perfil = {
    "nombre": input("Digite su nombre: "),
    "edad": int(input("Digite su edad: "))
}

# Actualizar la edad
nueva_edad = int(input("Digite la nueva edad: "))
perfil["edad"] = nueva_edad

# Añadir nueva clave "ciudad"
perfil["ciudad"] = input("Digite su ciudad: ")

# Mostrar diccionario final
print("\nPerfil final del usuario:")
print(perfil)
