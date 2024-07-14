a = input("Introduce un número entero: ")
a = int(a)

if a <= 1:
    print("Introduce un número mayor de 1.")
else: 
    primo = True
    for i in range(2, a):
        if a % i == 0:
            primo = False
            break

    if primo: 
        print(f"{a} es un número primo")
    else:
        print(f"{a} no es un número primo")


