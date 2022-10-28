# Crear una funcion contar vocales que reciba una palabra y cuente cuantas a tiene y asi con todas las vocales, que el usuario introduzca la palabra

palabra = str(input("Introduce una palabra: "))

def cuentaVocales(palabra):
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0
    for letra in palabra:
        if (letra == 'a') or (letra == 'A'):
            contador_a += 1
        elif (letra == 'e') or (letra == 'E'):
            contador_e += 1
        elif (letra == 'i') or (letra == 'I'):
            contador_i += 1
        elif (letra == 'o') or (letra == 'O'):
            contador_o += 1
        elif (letra == 'u') or (letra == 'U'):
            contador_u += 1
    print("Esta palabra tiene: ", f'', contador_a, "As", f'', contador_e, "Es", f'', contador_i, "Is", f'', contador_o, "Os", f'', contador_u, "Us")

cuentaVocales(palabra)