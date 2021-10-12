#Se ingresan tres valores por teclado, si todos son iguales
#  se imprime la suma del primero con el segundo y
#  a este resultado se lo multiplica por el tercero.
n=int(input("Ingrese un numero: "))
t=int(input("Ingrese un numero: "))
e=int(input("Ingrese un numero: "))

if n==t and n==e:
    suma=n+t
    print("La suma del primero y segundo: ",suma)
    pr=suma*e;
    print("La suma del primero y segundo multiplicado por el tercero: ",pr)
