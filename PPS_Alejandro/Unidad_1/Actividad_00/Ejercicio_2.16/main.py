# Definir una lista con nombres e imprimir aquellos que comienzan con la letra que deseemos

lista = ['Alvaro', 'Pedro', 'Juan', 'Anastasia', 'Amaral', 'Federico', 'Luis', 'fernando', 'ana']
letra = str(input("Dime una letra para ver todos los nombres de la lista que comienzan por esa letra: "))

def nombresConLetra(letra, lista):
    contador = 0                                                                    #Declaramos nuestro contador
    for palabra in lista:                                                           #Recorremos cada elemento de la lista
        if (letra == ((palabra[0]).upper())) or (letra == ((palabra[0]).lower())):  #Comprobamos la primera letra de cada elemento de la lista
            contador += 1                                                           #Sumamos 1 a nuestro contador cuando se cumpla la condicion anterior
    print(contador)

nombresConLetra(letra, lista)
