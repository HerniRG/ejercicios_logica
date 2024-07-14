# Solicitar al usuario que ingrese un número
a = input("Introduce un número: ")

# Convertir el valor de entrada a un entero
a = int(a)

# Determinar si el número es par o impar
if a % 2 == 0:
    print(f"El número {a} es par.")
else:
    print(f"El número {a} es impar.")
