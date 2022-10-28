# Define una funcion que devuelva una cadena invertida

cadena = "Hola mundo"

#print(''.join(reversed(cadena)))
#print((cadena[::-1]))

def reverse(cadena):
    cadenaInver = ""
    for i in cadena:
        cadenaInver = i + cadenaInver
    print(cadenaInver)

reverse(cadena)

def reverse2(cadena):
    cadenaVacia = ""
    for i in (cadena[::-1]):
        cadenaVacia = cadenaVacia + i
    print(cadenaVacia)

reverse2(cadena)
