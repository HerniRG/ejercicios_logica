# anagrama
# introducelo en una funcion
def comprobar_anagrama():

    p1 = input("Introduce palabra 1: ")
    p2 = input("Introduce palabra 2: ")

    p1 = p1.lower().strip(' ')
    p2 = p2.lower().strip(' ')

    p1 = sorted(p1)
    p2 = sorted(p2)

    if p1 == p2:
        print("Son anagramas")
        return True
    else:
        print("No son anagramas")
        return False


comprobar_anagrama()

