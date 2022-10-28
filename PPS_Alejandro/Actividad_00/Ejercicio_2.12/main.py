#Escribir una funcion que tome una lista de palabras y un entero n y devuelva las palabras que tengas mas de n caracteres

lista = ["Alvaro", "Raquel", "Alberto", "Ana", "Julian", "Cristina", "Cristiano ElBichoSiuuuuh"]
numero = int(input("Introduce un número: "))



def filtrar(lista,num):                     #Pedimos una lista de palabras y un numero
    listaPalabrasMas = []                   #Declaramos una lista vacia para añadir posteriormente las palabras que sean mas largas que el num
    for palabra in lista:                   #Recorremos la lista
        if len(palabra) > num:              #Si la longitud de la palabra es mayor que el num
            listaPalabrasMas.append(palabra)#Añadimos la palabra a la lista
    print(listaPalabrasMas)

filtrar(lista, numero)