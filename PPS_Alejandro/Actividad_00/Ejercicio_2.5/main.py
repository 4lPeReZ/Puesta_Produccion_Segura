# Crear una funcion que sume todos los numeros de una lista y otra que los multiplique

numeros = [1,2,3,4]

def suma(numeros):
    sumador = 0             #Declaramos nuestra variable que va a ir sumando los numero
    for i in numeros:       #Recorremos la lista en busca de enteros
        if type(i) == int:  #Comprobamos los de tipo int
            sumador += i    #Sumamos el valor a la variable
    print(sumador)

def multiplicador(numeros):
    sumador = 1             #Declaramos nuestra variable en 1 para que no multiplique x 0
    for i in numeros:       #Recorremos la lista en busca de enteros
        if type(i) == int:  #Comprobamos los de tipo int
            sumador *= i    #Multiplicamos el valor a la variable
    print(sumador)

multiplicador(numeros)
suma(numeros)