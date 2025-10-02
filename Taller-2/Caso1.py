# Lista inicial de usuarios registrados
usuarios_registrados = ["ana_dev", "luis_ux", "carlos_pm"]

# Conjunto para evitar duplicados
usuarios_unicos = set(usuarios_registrados)

print("=== Registro de usuarios ===")
print("Usuarios iniciales:", usuarios_registrados)

while True:
    nuevo_usuario = input("\nIngrese un nuevo usuario: ")

    if nuevo_usuario in usuarios_unicos:
        print(f" El usuario '{nuevo_usuario}' ya existe.")
    else:
        usuarios_registrados.append(nuevo_usuario)
        usuarios_unicos.add(nuevo_usuario)
        print(f" Usuario '{nuevo_usuario}' registrado con éxito.")

    opcion = input("¿Desea continuar registrando usuarios? (s/n): ").lower()

    if opcion == "n":
        print("\n=== Lista final de usuarios registrados (en orden) ===")
        print(usuarios_registrados)

        print("\n=== Conjunto de usuarios únicos ===")
        print(usuarios_unicos)

        print("\nAplicación cerrada")
        break
