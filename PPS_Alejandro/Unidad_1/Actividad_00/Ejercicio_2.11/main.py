# Escribir una funcion que tome una lista de palabras y devuelva la mas larga

lista = ["Alvaro", "Raquel", "Alberto", "Ana", "Julian", "Cristina", "Cristiano ElBichoSiuuuuh"]

def masLarga(lista):
    longitudMayor = 0                       #Definimos variables, longitud mas larga 0 y la palabra que sera mas larga en None
    palabraMasLarga = None

    for palabra in lista:                   #Recorreremos la lista de palabras 1 a 1
        if len(palabra) > longitudMayor:    #Si la longitud de la palabra es mayor que el valor que tiene actualmente la variable
            longitudMayor = len(palabra)    #Declararemos la longitud mayor la longitud de esa palabra
            palabraMasLarga = palabra       #Por lo que la palabra mas larga sera esta ultima palabra que hemos recorrido

    print(palabraMasLarga)

masLarga(lista)