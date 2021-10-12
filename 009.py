#Se ingresa por teclado un valor entero,
#  mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)
n=int(input("Ingrese su numero: "))
if n==0:
    print("es el 0")
else:
    if n>0:
        print("es un valor a positivo")
    else:
        print("es un valor a negativo")
