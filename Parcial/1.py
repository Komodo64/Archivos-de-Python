carrito = []

while True:
    print("\nOpciones:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver carrito")
    print("4. Salir")

    eleccion = input("Elige una opción (1-4): ")

    if eleccion == "1":
        producto = input("Ingresa el nombre del producto a agregar: ")
        carrito.append(producto)
        print(f"{producto} agregado al carrito.")

    elif eleccion == "2":
        producto = input("Ingresa el nombre del producto a eliminar: ")
        if producto in carrito:
            carrito.remove(producto)
            print(f"{producto} eliminado del carrito.")
        else:
            print(f"{producto} no está en el carrito.")

    elif eleccion == "3":
        if carrito:  # si la lista NO está vacía
            print("Contenido del carrito:")
            for i, prod in enumerate(carrito, start=1):
                print(f"{i}. {prod}")
        else:
            print("El carrito está vacío.")

    elif eleccion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, elige de nuevo.")
