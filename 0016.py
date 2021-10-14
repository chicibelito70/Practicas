#Escribir un programa que solicite ingresar 10 notas de alumnos y
#  nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

con=0
n=0
t=0
while t<=10:
    nota=int(input("ingrese un numero: "))
    if nota>=7:
        con=con+1
    else:
        n=n+1
    t=t+1
print("Cantidad de alumnos con notas mayores o iguales a 7 es:",con)
print("Cantidad de alumons con notas menores a 7 es: ",n)

