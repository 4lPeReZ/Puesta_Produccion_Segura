# Crear una funcion contar vocales que reciba una palabra y cuente cuantas a tiene y asi con todas las vocales, que el usuario introduzca la palabra

palabra = str(input("Introduce una palabra: "))

def cuentaVocales(palabra):
    contador_a = 0                                  #Contadores para las diferentes vocales
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0
    for letra in palabra:                           #Recorremos cada letra de la palabra introducida por el usuario
        if (letra == 'a') or (letra == 'A'):        #Condicion de la letra a mayuscula o minuscula
            contador_a += 1                         #Sumamos 1 a nuestro contador
        elif (letra == 'e') or (letra == 'E'):      #Condicion de la letra e mayuscula o minuscula
            contador_e += 1                         #Sumamos 1 a nuestro contador
        elif (letra == 'i') or (letra == 'I'):      #Condicion de la letra i mayuscula o minuscula
            contador_i += 1                         #Sumamos 1 a nuestro contador
        elif (letra == 'o') or (letra == 'O'):      #Condicion de la letra o mayuscula o minuscula
            contador_o += 1                         #Sumamos 1 a nuestro contador
        elif (letra == 'u') or (letra == 'U'):      ##Condicion de la letra u mayuscula o minuscula
            contador_u += 1                         #Sumamos 1 a nuestro contador
    print("Esta palabra tiene: ", f'', contador_a, "As", f'', contador_e, "Es", f'', contador_i, "Is", f'', contador_o, "Os", f'', contador_u, "Us")

cuentaVocales(palabra)