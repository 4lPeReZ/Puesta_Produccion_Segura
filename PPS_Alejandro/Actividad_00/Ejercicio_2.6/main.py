# Define una funcion que devuelva una cadena invertida

cadena = "Hola mundo"

#print(''.join(reversed(cadena)))
#print((cadena[::-1]))

def reverse(cadena):
    cadenaInver = ""                    #Declaramos la variable vacia
    for i in cadena:                    #Recorremos la cadena
        cadenaInver = i + cadenaInver   #Escribimos el elemento mas el estado anterior de la variable
    print(cadenaInver)

reverse(cadena)

def reverse2(cadena):
    cadenaVacia = ""
    for i in (cadena[::-1]):            #Comenzamos el bucle por el final de la cadena, es decir el final
        cadenaVacia = cadenaVacia + i   #Vamos rellenando nuestra variable con cada iteracion del bucle
    print(cadenaVacia)

reverse2(cadena)
