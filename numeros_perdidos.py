"""
Dado un array de enteros ordenado y sin repetidos,
crea una función que calcule y retorne todos los que faltan entre
el mayor y el menor.
"""

listado = [-1, 7, 8, 12, 19, 65]
listado_faltantes = []

for i in range(listado[0], listado[(len(listado)-1)], 1):
    if i not in listado:
        listado_faltantes.append(i)

print(listado_faltantes)