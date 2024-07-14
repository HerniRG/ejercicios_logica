
def esBisiesto(anio):
    if anio%400 == 0:
        return True
    elif anio%100 == 0:
        return False
    elif anio%4 == 0:
        return True
    else:
        return False
    

print(esBisiesto(2023))
