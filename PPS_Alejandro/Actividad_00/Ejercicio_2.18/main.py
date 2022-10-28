# Escribe una funcion que determine si un año es bisisesto o no

año = int(input("Introduce un año: "))

def bisiesto(año):
    if ((año % 4) == 0) and (((año % 400) == 0) or ((año % 100) != 0)):
        print("El año ",año," es bisiesto")
    else:
        print("El año ",año," no es bisiesto")

bisiesto(año)