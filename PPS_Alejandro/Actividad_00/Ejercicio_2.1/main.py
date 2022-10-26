# Definir una funcion max()
# que tome como argumento dos numeros y devuelve el mayor de ellos.

num1=int(input("Introduce un número: "))
num2=int(input("Introduce otro número: "))

def maximo(num1, num2):
    if num1 < num2:
        print(num2, " Es el número mayor")
    elif num2 < num1:
        print(num1, " Es el número mayor")
    elif num1 == num2:
        print("Son iguales")
    else:
        print("Alguno de los datos es inválido")

maximo(num1,num2)