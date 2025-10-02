# Árbol Genealógico con diccionarios

# Árbol inicial (3 generaciones)
familia = {
    "nombre": "Carlos",
    "edad": 70,
    "hijos": [
        {
            "nombre": "Ana",
            "edad": 45,
            "hijos": [
                {"nombre": "Luis", "edad": 20, "hijos": []},
                {"nombre": "María", "edad": 18, "hijos": []}
            ]
        },
        {
            "nombre": "Pedro",
            "edad": 40,
            "hijos": [
                {"nombre": "Javier", "edad": 15, "hijos": []}
            ]
        }
    ]
}

# ---------------- FUNCIONES ----------------

# Mostrar el árbol con indentación
def mostrar_arbol(nodo, nivel=0):
    indentacion = "  " * nivel
    print(f"{indentacion}👤 {nodo['nombre']} ({nodo['edad']} años)")
    for hijo in nodo.get("hijos", []):
        mostrar_arbol(hijo, nivel + 1)


# Buscar persona por nombre
def buscar_persona(nodo, nombre):
    if nodo["nombre"] == nombre:
        return nodo
    for hijo in nodo.get("hijos", []):
        encontrado = buscar_persona(hijo, nombre)
        if encontrado:
            return encontrado
    return None


# Agregar persona como hijo de otra
def agregar_persona(nodo, nombre_padre, nueva_persona):
    padre = buscar_persona(nodo, nombre_padre)
    if padre:
        padre["hijos"].append(nueva_persona)
        return True
    return False


# Calcular promedio de edad de toda la familia
def calcular_promedio_edad(nodo):
    def recorrer(n):
        total = n["edad"]
        cantidad = 1
        for hijo in n.get("hijos", []):
            t, c = recorrer(hijo)
            total += t
            cantidad += c
        return total, cantidad
    
    total, cantidad = recorrer(nodo)
    return total / cantidad if cantidad > 0 else 0


# ---------------- PRUEBAS ----------------
print("👪 Árbol genealógico:")
mostrar_arbol(familia)

print("\n🔍 Buscar a 'Ana':")
print(buscar_persona(familia, "Ana"))

print("\n➕ Agregando un nuevo hijo a Pedro...")
agregar_persona(familia, "Pedro", {"nombre": "Lucía", "edad": 10, "hijos": []})

print("\n👪 Árbol genealógico actualizado:")
mostrar_arbol(familia)

print("\n📊 Promedio de edad:", calcular_promedio_edad(familia))
