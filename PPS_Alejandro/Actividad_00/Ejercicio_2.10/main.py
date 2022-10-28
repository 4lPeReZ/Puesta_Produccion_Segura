# Escribir una funcion que tome una lista de numeros y devuelva el mayor de todos ellos

lista = [1,2,3,4,5,6,7,8,9,10]

def numMayor(lista):
    listaOrdenada = sorted(lista)       #Ordenamos la lista
    print(listaOrdenada[-1])            #Cogemos el ultimo elemento de la lista ordenada

numMayor(lista)