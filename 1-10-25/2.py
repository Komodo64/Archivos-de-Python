# Árbol Binario de Búsqueda (BST) con clases
# Los valores menores van a la izquierda, mayores a la derecha

class Nodo:
    # Clase que representa un nodo individual del árbol
    def __init__(self, valor):
        self.valor = valor  # Dato almacenado en el nodo
        self.izquierdo = None  # Referencia al hijo izquierdo
        self.derecho = None  # Referencia al hijo derecho

class ArbolBinarioBusqueda:
    # Clase que representa el árbol completo
    def __init__(self):
        self.raiz = None  # Inicialmente el árbol está vacío
    
    def insertar(self, valor):
        # Método público para insertar un valor
        if self.raiz is None:
            self.raiz = Nodo(valor)  # Si el árbol está vacío, crear raíz
        else:
            self._insertar_recursivo(self.raiz, valor)  # Insertar recursivamente
    
    def _insertar_recursivo(self, nodo, valor):
        # Método privado para insertar recursivamente
        if valor < nodo.valor:  # Si es menor, va a la izquierda

              if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)  # Crear nuevo nodo
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)  # Seguir buscando
        else:  # Si es mayor o igual, va a la derecha
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)  # Crear nuevo nodo
            else:
                self._insertar_recursivo(nodo.derecho, valor)  # Seguir buscando
    
    def buscar(self, valor):
        # Buscar un valor en el árbol
        return self._buscar_recursivo(self.raiz, valor)
    
     def _buscar_recursivo(self, nodo, valor):
        # Método privado para buscar recursivamente
        if nodo is None:
            return False  # No se encontró el valor
        if nodo.valor == valor:
            return True  # Se encontró el valor
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)  # Buscar a la izquierda
        else:
            return self._buscar_recursivo(nodo.derecho, valor)  # Buscar a la derecha
    
    def inorden(self):
        # Recorrido inorden: izquierda-raíz-derecha (muestra valores ordenados)
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _inorden_recursivo(self, nodo, resultado):
        # Método privado para recorrido inorden
        if nodo:
            self._inorden_recursivo(nodo.izquierdo, resultado)  # Visitar izquierda
            resultado.append(nodo.valor)  # Visitar raíz
            self._inorden_recursivo(nodo.derecho, resultado)  # Visitar derecha

# Crear y usar el árbol
arbol = ArbolBinarioBusqueda()
valores = [50, 30, 70, 20, 40, 60, 80]

# Insertar valores en el árbol
for valor in valores:
    arbol.insertar(valor)

# Mostrar valores ordenados
print("Valores en orden:", arbol.inorden())  # [20, 30, 40, 50, 60, 70, 80]

# Buscar valores
print("¿Está el 40?", arbol.buscar(40))  # True
print("¿Está el 100?", arbol.buscar(100))  # False

# Árbol N-ario (cada nodo puede tener múltiples hijos) con diccionarios
# Representa un sistema de archivos

# Crear estructura de carpetas y archivos
sistema_archivos = {
    'nombre': 'raiz',  # Nombre del directorio
    'tipo': 'carpeta',  # Tipo de nodo
    'hijos': [  # Lista de hijos (subcarpetas y archivos)
        {
            'nombre': 'documentos',
            'tipo': 'carpeta',
            'hijos': [
                {'nombre': 'trabajo.pdf', 'tipo': 'archivo', 'tamaño': 150},
                {'nombre': 'personal.docx', 'tipo': 'archivo', 'tamaño': 80}
            ]
        },
        {
            'nombre': 'imagenes',
            'tipo': 'carpeta',
            'hijos': [
                {'nombre': 'foto1.jpg', 'tipo': 'archivo', 'tamaño': 200},
                {'nombre': 'foto2.png', 'tipo': 'archivo', 'tamaño': 300}
            ]
        },
        {'nombre': 'readme.txt', 'tipo': 'archivo', 'tamaño': 10}
    ]
}


# Función para mostrar la estructura del árbol con indentación
def mostrar_arbol(nodo, nivel=0):
    # Crear indentación según el nivel de profundidad
    indentacion = "  " * nivel
    
    # Mostrar información del nodo actual
    if nodo['tipo'] == 'carpeta':
        print(f"{indentacion}📁 {nodo['nombre']}/")
    else:
        print(f"{indentacion}📄 {nodo['nombre']} ({nodo['tamaño']} KB)")
    
    # Recorrer recursivamente los hijos si existen
    if 'hijos' in nodo:
        for hijo in nodo['hijos']:
            mostrar_arbol(hijo, nivel + 1)

# Función para calcular el tamaño total del árbol
def calcular_tamaño(nodo):
    # Si es un archivo, devolver su tamaño
    if nodo['tipo'] == 'archivo':
        return nodo['tamaño']
    
    # Si es carpeta, sumar el tamaño de todos los hijos
    tamaño_total = 0
    if 'hijos' in nodo:
        for hijo in nodo['hijos']:
            tamaño_total += calcular_tamaño(hijo)
    
    return tamaño_total

# Función para mostrar la estructura del árbol con indentación
def mostrar_arbol(nodo, nivel=0):
    # Crear indentación según el nivel de profundidad
    indentacion = "  " * nivel
    
    # Mostrar información del nodo actual
    if nodo['tipo'] == 'carpeta':
        print(f"{indentacion}📁 {nodo['nombre']}/")
    else:
        print(f"{indentacion}📄 {nodo['nombre']} ({nodo['tamaño']} KB)")
    
    # Recorrer recursivamente los hijos si existen
    if 'hijos' in nodo:
        for hijo in nodo['hijos']:
            mostrar_arbol(hijo, nivel + 1)

# Función para calcular el tamaño total del árbol
def calcular_tamaño(nodo):
    # Si es un archivo, devolver su tamaño
    if nodo['tipo'] == 'archivo':
        return nodo['tamaño']
    
    # Si es carpeta, sumar el tamaño de todos los hijos
    tamaño_total = 0
    if 'hijos' in nodo:
        for hijo in nodo['hijos']:
            tamaño_total += calcular_tamaño(hijo)
    
    return tamaño_total

# Mostrar la estructura del sistema de archivos
print("Estructura del sistema de archivos:")
mostrar_arbol(sistema_archivos)

# Calcular y mostrar el tamaño total
tamaño = calcular_tamaño(sistema_archivos)
print(f"\nTamaño total: {tamaño} KB")  # Salida: 740 KB