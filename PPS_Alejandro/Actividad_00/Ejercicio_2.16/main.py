# Definir una lista con nombres e imprimir aquellos que comienzan con la letra que deseemos

lista = ['Alvaro', 'Pedro', 'Juan', 'Anastasia', 'Amaral', 'Federico', 'Luis', 'fernando', 'ana']
letra = str(input("Dime una letra para ver todos los nombres de la lista que comienzan por esa letra: "))

def nombresConLetra(letra, lista):
    contador = 0
    for palabra in lista:
        if (letra == ((palabra[0]).upper())) or (letra == ((palabra[0]).lower())):
            contador += 1
    print(contador)

nombresConLetra(letra, lista)
