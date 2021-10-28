#Elaborar una función que reciba tres enteros y nos retorne el valor
#  promedio de los mismos

def enteros(u,y,t):
   
    prom=(u+y+t)//3
    return prom

#principla

u=int(input("Ingrese un numero: "))
y=int(input("Ingrese un numero: "))
t=int(input("Ingrese un numero: "))

print("Valor promedio de los tres numeros", enteros(u,y,t))