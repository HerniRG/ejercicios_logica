"""
Dado un listado de números, encuentra el SEGUNDO más grande
"""
listado = [4, 5, 6, -9, 12, 77]

# Ordenar la lista en orden descendente
listado.sort(reverse=True)

# Imprimir el segundo número más grande
print("El segundo número más grande es:", listado[1])