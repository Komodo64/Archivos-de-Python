# Función para buscar un archivo en el sistema de archivos
def buscar_archivo(nodo, nombre_archivo):
    # Si es un archivo, compara el nombre
    if nodo['tipo'] == 'archivo':
        return nodo['nombre'] == nombre_archivo
    
    # Si es carpeta, buscar en los hijos
    if 'hijos' in nodo:
        for hijo in nodo['hijos']:
            if buscar_archivo(hijo, nombre_archivo):
                return True
    
    return False
