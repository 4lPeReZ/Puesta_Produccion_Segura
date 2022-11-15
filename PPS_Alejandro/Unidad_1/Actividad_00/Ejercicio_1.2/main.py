numero1 = int(input("Introduzca un primer valor: "))
numero2 = int(input("Introduzca un segundo valor: "))

if numero1 < numero2:
    print("El número mayor es: ",numero2)
elif numero2 < numero1:
    print("El número mayor es: ",numero1)
elif numero1 == numero2:
    print("Son iguales")
else:
    print("Datos inválidos")