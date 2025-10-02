# Contar hojas en un árbol N-ario
def contar_hojas(nodo):
    # Caso base: si es archivo => es hoja
    if nodo['tipo'] == 'archivo':
        return 1
    
    # Si es carpeta y no tiene hijos => también es hoja
    if nodo['tipo'] == 'carpeta' and ('hijos' not in nodo or len(nodo['hijos']) == 0):
        return 1
    
    # Si tiene hijos, sumar las hojas de cada hijo
    hojas = 0
    if 'hijos' in nodo:
        for hijo in nodo['hijos']:
            hojas += contar_hojas(hijo)
    
    return hojas
