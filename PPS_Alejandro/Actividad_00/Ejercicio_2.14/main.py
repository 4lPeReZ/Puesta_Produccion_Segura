# Contruir un programa que convierta binarios a enteros
# EXTRA Pedir al usuario el año actual, se pide nombre y año de nacimiento de 3 personas y imprimir cuantos años les toca cumplir en ESTE año

numeroBinario = int('11101', 2)
print(numeroBinario)

def binarioDecimal(binario):
    decimal = 0
    for posicion, digitoStr in enumerate(binario[::-1]):
        decimal += int(digitoStr) * 2 ** posicion
    print(decimal)

binarioDecimal('101')
binarioDecimal('100011')

# EXTRA
print(f'')

def cumpleAños():
    añoAct = int(input("Introduce el año actual: "))

    nombre_1 = str(input("Introduce un nombre: "))
    añoNac_1 = int(input("Introduce el año de nacimiento: "))
    cumple_1 = añoAct - añoNac_1
    print(nombre_1, "cumplira este año: ", cumple_1)

    nombre_2 = str(input("Introduce un nombre: "))
    añoNac_2 = int(input("Introduce el año de nacimiento: "))
    cumple_2 = añoAct - añoNac_2
    print(nombre_2, "cumplira este año: ", cumple_2)

    nombre_3 = str(input("Introduce un nombre: "))
    añoNac_3 = int(input("Introduce el año de nacimiento: "))
    cumple_3 = añoAct - añoNac_3
    print(nombre_3, "cumplira este año: ", cumple_3)

cumpleAños()