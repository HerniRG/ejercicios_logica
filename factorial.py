# Solicitar al usuario que ingrese un número entero no negativo
a = input("Introduce un número entero no negativo: ")

# Convertir el valor de entrada a un entero

while True:
    try:
        a = int(a)
        break
    except ValueError:
        print("Por favor, introduce un número entero no negativo.")
        a = input("Introduce un número entero no negativo: ")


# Verificar que el número sea no negativo
if a < 0:
    print("Por favor, introduce un número entero no negativo.")
else:
    # Inicializar la variable para el factorial
    fact = 1
    
    # Calcular el factorial usando un bucle for
    for i in range(1, a + 1):
        fact *= i
    
    # Imprimir el resultado
    print(f"El factorial de {a} es {fact}.")
