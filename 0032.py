#Almacenar en una lista los sueldos (valores float) de 5 operarios. 
# Imprimir la lista y el promedio de sueldos

suel=[]
n=0
for x in range(5):
    p=float(input("Ingrese su sueldos: "))
    suel.append(p)
    n=n+p
print("------------------------------------")
print("La lista de los sueldos es: ",suel)
print("------------------------------------")
prom=n/5
print("El promedio de los suedo es: ",prom)