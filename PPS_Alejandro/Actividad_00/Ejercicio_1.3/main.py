# Iterar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3

for valor in range(0,11):
    if valor % 3 == 0:
        print(valor)

# Si quisieramos saber todos los número divisibles por 3 en un rango amplio sería asi:
# numero = 0
# limite_numero = 1000
# while numero < limite_numero:
#   if numero % 3:
#       print(numero, " es multiplo de 3")
#   numero=numero+1