#Realizar un programa que solicite la carga por teclado de dos números, 
# si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar 
# el producto y la división del primero respecto al segundo.

n=int(input("Ingrese un numero: "))
e=int(input("Ingrese un numero: "))

if n>e:
    r=e+n 
    print("la suma de los numero es:    ",r)
    q=e-n
    print("La resta de los numeros es:  ",q)
else:
    t=n*e
    print("La multiplicacion del los numero es:   ",t)
    y=n/e
    print("La division de los numero es:    ",y)
    