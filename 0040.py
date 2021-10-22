#Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla.
pais=[]
for x in range(5):
    pa=input("Ingrese nombre de paises: ")
    pais.append(pa)
for k in range(4):
    for x in range(4-k):
        if pais[x]>pais[x+1]:
            aux=pais[x]
            pais[x]=pais[x+1]
            pais[x+1]=aux
print("-------------------------")
print("Listados de paises: ",pais)