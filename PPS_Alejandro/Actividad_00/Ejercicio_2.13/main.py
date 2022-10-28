# Escribir un programa que pida al usuario una cadena y el programa devuelva cuantas mayusculas tiene

cadena = str(input("Introduzca una cadena: "))

def mayusMinus(cadena):
    indice = 0                                  #Indice que va a recorrer 1 a 1 las letras de la cadena
    mayusculas = 0                              #Contador mayusculas
    minusculas = 0                              #Contador minusculas
    while indice < len(cadena):                 #Bucle que mientras el indice sea menos que la longitud de la cadena se sigue ejecutando el bucle
        letra = cadena[indice]                  #Capturamos la letra en una variable
        if letra.isupper() == True:             #Comprobamos si esa letra es mayusculas
            mayusculas += 1                     #Si es mayus sumamos 1
        else:
            minusculas += 1                     #Si es minus sumamos 1
        indice += 1                             #Cuando acabemos sumamos 1 al indice y comenzamos con la siguiente letra
    print("Total de mayusculas: ", mayusculas)
    print("Total de minusculas: ", minusculas)

mayusMinus(cadena)