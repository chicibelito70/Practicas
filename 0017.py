#Se ingresan un conjunto de n alturas de personas por teclado.
#  Mostrar la altura promedio de las personas.

x=1
sum=0
n=int(input("Cuantas personas hay:"))
while x<=n:
    al=float(input("Ingrese su altura: "))
    sum=sum+al
    x=x+1
prom=sum/n
print("La altura es: ", prom)