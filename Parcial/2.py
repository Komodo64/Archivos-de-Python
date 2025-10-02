# Conjunto con los roles válidos que se pueden asignar
roles_validos = {"admin", "editor", "visitante"}

# Lista vacía donde se guardarán los usuarios registrados con su rol
usuarios_registrados = []

# Bucle infinito: sigue pidiendo datos hasta que el usuario escriba "salir"
while True:
    # Pedimos el nombre de usuario
    nombre_usuario = input("Ingresa el nombre de usuario (o 'salir' para terminar): ")
    
    # Si el usuario escribe "salir", se rompe el bucle y deja de registrar
    if nombre_usuario.lower() == "salir":
        break

    # Pedimos el rol que tendrá el usuario
    rol_usuario = input("Ingresa el rol (admin, editor, visitante): ").lower()

    # Verificamos si el rol está dentro del conjunto de roles válidos
    if rol_usuario in roles_validos:
        # Si el rol es válido, guardamos una tupla (usuario, rol) en la lista
        usuarios_registrados.append((nombre_usuario, rol_usuario))
        print(f"Usuario '{nombre_usuario}' registrado como '{rol_usuario}'.")
    else:
        # Si el rol no está en roles_validos, mostramos un mensaje de error
        print("Error: Rol no válido. Intenta nuevamente.")

# Al salir del bucle, mostramos todos los usuarios registrados
print("\nUsuarios registrados:")
for usuario in usuarios_registrados:
    print(usuario)
