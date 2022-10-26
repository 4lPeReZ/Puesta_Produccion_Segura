# Definir una funcion que calcule la longitud de una lista o una cadena.

vocales = ['a','e','i','o','u']
cadena = "Hola mundo"

def longLista(lista):
    if type(lista) == list:
        longitud = 0    #Contador de la longitud de la lista
        for i in lista: #Bucle ue va haciendo iteraciones recorriendo la lista
            longitud+=1 #Suma 1 al contador por cada iteracion que hace recorriendo la lista
        return print(longitud)
    elif type(lista) == str:
        longitud = 0
        for i in lista:
            longitud+=1
        return print(longitud)
    else:
        print("No es ni una cadena ni una lista")

longLista(vocales)
longLista(cadena)