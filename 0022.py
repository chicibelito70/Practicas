#Desarrollar un programa que solicite la carga de 10 números
#  e imprima la suma de los últimos 5 valores ingresados

r=0
for n in range(10):
    v=int(input("Ingrese un valor:"))
    if n>4:
        r=r+v
print("La suma de los últimos 5 valores es: ",r)