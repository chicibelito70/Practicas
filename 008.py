#Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.
num1=int(input("Ingrese un valor:  "))
num2=int(input("Ingrese un valor:  "))
num3=int(input("Ingrese un valor:  "))
if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)