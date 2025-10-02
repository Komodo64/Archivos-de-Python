# Diccionario vacío donde se guardarán los contactos
# La clave será el nombre, y el valor será el número de teléfono
agenda = {}

# Bucle infinito para mostrar siempre el menú hasta que el usuario elija salir
while True:
    # Menú de opciones
    print("\nOpciones:")
    print("1. Agregar contacto")
    print("2. Buscar teléfono por nombre")
    print("3. Mostrar todos los contactos")
    print("4. Salir")

    # Pedimos al usuario que seleccione una opción
    opcion = input("Elige una opción (1-4): ")

    # Opción 1 → Agregar contacto
    if opcion == "1":
        nombre = input("Ingresa el nombre del contacto: ")
        telefono = input("Ingresa el teléfono del contacto: ")
        # Guardamos el contacto en el diccionario: {nombre: teléfono}
        agenda[nombre] = telefono
        print(f"Contacto {nombre} agregado.")

    # Opción 2 → Buscar un contacto por nombre
    elif opcion == "2":
        nombre = input("Ingresa el nombre del contacto a buscar: ")
        # Usamos get() para buscar el nombre en el diccionario
        # Si no existe, devuelve None en lugar de dar error
        telefono = agenda.get(nombre)
        if telefono:
            print(f"Teléfono de {nombre}: {telefono}")
        else:
            print("Contacto no encontrado.")

    # Opción 3 → Mostrar todos los contactos
    elif opcion == "3":
        print("Lista de contactos:")
        # Recorremos el diccionario con items() → devuelve pares (clave, valor)
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")

    # Opción 4 → Salir del programa
    elif opcion == "4":
        print("Saliendo de la agenda.")
        break  # Rompe el bucle while y termina el programa

    # Si se escribe algo fuera de 1-4 → opción inválida
    else:
        print("Opción no válida. Intenta nuevamente.")
