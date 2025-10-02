mis_sugerencias = ["París", "Roma", "Berlín"]

sugerencias_amigo = ["Londres", "Roma", "Praga"]

set_mio = set(mis_sugerencias)

set_amigo = set(sugerencias_amigo)

destinos_finales = set_mio.union(set_amigo)

print("\n Destinos finales del viaje:", destinos_finales)
print(f" Número total de destinos únicos: {len(destinos_finales)}")