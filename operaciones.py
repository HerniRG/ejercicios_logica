
def pedir_numeros():
    strN1 = input('Introduzca el primer número: ')
    strN2 = input('Introduzca el segundo número: ')
    return strN1, strN2

def comprobar_numeros(strN1, strN2):
    return strN1.isdigit() and strN2.isdigit()



strN1, strN2 = pedir_numeros()

while not comprobar_numeros(strN1, strN2):
    print('Por favor, introduzca dos números enteros')
    strN1, strN2 = pedir_numeros()

n1 = int(strN1)
n2 = int(strN2)

n1 = n1 / 10
n2 = n2 / 10

suma = round(n1 + n2, 2)
resta = round(n1 - n2, 2)
multiplicacion = round(n1 * n2,2)
division = round(n1 / n2, 2)

print('La suma es: ' + str(suma))
print('La resta es: ' + str(resta))
print('La multiplicación es: ' + str(multiplicacion))
print('La división es: ' + str(division))
