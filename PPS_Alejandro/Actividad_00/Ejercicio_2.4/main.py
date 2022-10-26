# Escribe una funcion que tome un caracter y devuelva True si es una vocal o False si es consonante

caracter = input("Introduce un carácter: ")  #Es una variable de tipo string
vocales = ['a','e','i','o','u']             #Lista con vocales

def vocal(caracter):
    if len(caracter) == 1:                      #Comprobamos que se ha introducido solo 1 caracter
        if type(caracter) == str:               #Miramos el tipo del input, por si acaso
            if caracter in vocales:             #Comprobamos si el caracter esta en la lista de vocales
                print(True)
            else:
                print(False)
        else:                                   #Si no fuera una variable de tipo string nos devuelve lo siguiente
            print("No es un carácter de tipo string")
    else:
        print("Has introducido más de un carácter")

vocal(caracter)
