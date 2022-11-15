# Definir una tupla con 10 edades de personas, imprimir la cantidad de personas con edad superior a 20, pedir edades por teclado

tupla = (10, 18, 19, 20, 25, 30, 67, 80)

def edades(tupla):
    contador = 0                #Establecemos un contador
    for i in tupla:             #Recorremos la tupla
        if i > 20:              #Establecemos la condicion que sea mayor de 20 años
            contador += 1       #Sumamos 1 al contador cuando se cumpla la condicion
    print(contador)

edades(tupla)