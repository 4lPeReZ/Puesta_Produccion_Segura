# Hacer un histograma definiendo una funcion que tome una lista de numero enteros

notas = [1,2,3,4,5,6,7,8,9,10,4,5,6,3,2,2,2,5,8,9,5,5,4,10]

def procedimiento(notas):               #Hay 10 intervalos ya que hay 10 notas diferentes
    mapa_notas = {}                     #Definimos un diccionario vacio
    for nota in notas:                  #Recorremos nuestra lista
        if nota in mapa_notas:          #Si la nota existe en el diccionario sumamos 1 a la clave de ese valor
            mapa_notas[nota] += 1
        else:                           #Si la nota no existe en ese diccionario le indicamos que la clave de ese valor es 1
            mapa_notas[nota] = 1

    for i in sorted(mapa_notas):        #Recorremos cada uno de los elementos del diccionario, que seran 10 ya que son las notas diferentes
        print(f'{i}: {mapa_notas[i]}')  #Va imprimiendo elemento a elementos con su clave

procedimiento(notas)