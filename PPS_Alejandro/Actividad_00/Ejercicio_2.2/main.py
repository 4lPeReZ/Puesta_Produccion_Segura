# Definir una funcion para que tome 3 argumentos y nos devuelva el mayor de ellos

print("Introduce 3 valores numericos y te devolveré el mayor de ellos")

n1=int(input("Introduce el primer valor: "))
n2=int(input("Introduce el segundo valor: "))
n3=int(input("Introduce el primer valor: "))

def mayorTres(n1, n2, n3):
    if (n1 <= n2) and (n2 >= n3):
        print("El mayor es: ", n2)
    elif (n1 >= n2) and (n1 >= n3):
        print("El mayor es: ", n1)
    elif (n1 <= n3) and (n2 <= n3):
        print("El mayor es: ", n3)
    elif (n1==n2) and (n2==n3):
        print("Los numeros son iguales")
    else:
        print("Algún dato introducido es incorrecto")

mayorTres(n1,n2,n3)