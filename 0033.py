#Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
#Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y 
# cuántas más bajas.

alt=[]
sum=0
for x in range(5):
    w=float(input("Ingrese su altura: "))
    alt.append(w)
    sum=sum+w
print("------------------------------------")
print("La lista de las alturas es: ",alt)
print("------------------------------------")
prom=w/5
print("El promedio de las alturas es: ",prom)
print("----------------------------------------")


baja=0
altas=0

for x in range(5):
    if alt[x]>prom:
        altas=altas+1
    else:
        if alt[x]<prom:
            baja=baja+1
print("La cantidad de personas mas bajas al promedio es: ",baja)
print("-----------------------------------------------------------")
print("La cantidad de personas mas altas al promedio es: ",altas)
