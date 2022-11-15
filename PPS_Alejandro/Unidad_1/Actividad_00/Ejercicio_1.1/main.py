num = int(input("Introduzca un número de calificación: "))

if (9<= num) and (num <= 10):
    print("A")
elif (8<= num) and (num < 9):
    print("B")
elif (7 <= num) and (num < 8):
    print("C")
elif (6<= num) and (num < 7):
    print("D")
elif (0<= num) and (num < 6):
    print("F")
else:
    print("El número no esta comprendido entre 0 y 10")