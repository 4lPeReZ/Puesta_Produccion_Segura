# Define una funcion llamada superposicion que tome dos listas y devuelva True si tienen al menos un miembro en común
# Escribir la funcion usando un bucle anidado

lista_1 = [1,2,3,4]
lista_2 = [1,7,5]

def superposicion(lista_1, lista_2):
    for i in lista_1:               #Bucle que recorre elemento a elemento la primera lista
        for j in lista_2:           #Bucle que recorre elemento a elemento la segunda lista
            if i == j:              #Compara uno a uno los elementos de ambas listas
                return (True)       #Rompe el bucle si se cumple la condicion y retorna True
    return (False)                  #Si no cumple la condicion retorna un False

print(superposicion(lista_1,lista_2))