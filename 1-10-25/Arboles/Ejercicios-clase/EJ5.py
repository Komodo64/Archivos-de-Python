# Árbol balanceado
raiz = Nodo(1)
raiz.izq = Nodo(2)
raiz.der = Nodo(3)
raiz.izq.izq = Nodo(4)
raiz.izq.der = Nodo(5)

print("Árbol balanceado:", esta_balanceado(raiz))  # True

# Árbol NO balanceado
raiz_no = Nodo(1)
raiz_no.izq = Nodo(2)
raiz_no.izq.izq = Nodo(3)
raiz_no.izq.izq.izq = Nodo(4)

print("Árbol balanceado:", esta_balanceado(raiz_no))  # False
 