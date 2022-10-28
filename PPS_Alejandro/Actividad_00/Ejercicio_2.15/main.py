# Definir una tupla con 10 edades de personas, imprimir la cantidad de personas con edad superior a 20, pedir edades por teclado

tupla = (10, 18, 19, 20, 25, 30, 67, 80)

def edades(tupla):
    contador = 0
    for i in tupla:
        if i > 20:
            contador += 1
    print(contador)

edades(tupla)