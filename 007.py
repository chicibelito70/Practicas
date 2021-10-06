#Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) 
# mostrar un mensaje indicando si el número tiene uno o dos dígitos.
#(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

n=int(input("Ingrese un numero positivo:    "))
if n>10:
    print("Numero de dos digitos")
else:
    print("este numero no  es de dos digitos")
