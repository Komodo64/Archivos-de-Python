class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def altura_arbol(root):
    """
    Devuelve la altura (profundidad máxima) de un árbol binario.
    Convención: árbol vacío -> 0, solo raíz -> 1.
    """
    if root is None:
        return 0
    # 1 + max(altura subárbol izquierdo, altura subárbol derecho)
    return 1 + max(altura_arbol(root.left), altura_arbol(root.right))

# Ejemplo
#      A
#     / \
#    B   C
#   /
#  D
n = Node("A", Node("B", Node("D")), Node("C"))
print(altura_arbol(n))  # salida esperada: 3
