# Definir una funcion que tome un entero cualquiera y un caracter y devuelva el caracter multiplicado por el entero

entero = int(input("Introduce un número: "))
caracter = str(input("Introduce un caracter: "))

def generarCaracter(entero, caracter):
        print(entero*caracter)

generarCaracter(entero, caracter)