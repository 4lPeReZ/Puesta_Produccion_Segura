# Escribe una funcion que determine si un año es bisisesto o no

año = int(input("Introduce un año: "))

def bisiesto(año):
    if ((año % 4) == 0) and (((año % 400) == 0) or ((año % 100) != 0)): #Condicion de si el año es divisible entre 4 y 400 y su resto es 0
        print("El año ",año," es bisiesto")                             #O si es divisible entre 100 pero el resto no es 0
    else:
        print("El año ",año," no es bisiesto")

bisiesto(año)