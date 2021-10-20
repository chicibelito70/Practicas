#Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si 
# se repite dentro de la lista 
# (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)

lis=[]
for x in range(5):
    e=int(input("Ingrese su valor: "))
    lis.append(e)
mayor=lis[0]
for x in range(1,5):
    if lis[x]>mayor:
        mayor=lis[x]
print("Lista completa es: ",lis)
print("----------------------")
print("Mayor en la lista es: ",mayor)

cantidad=0
for x in range(5):
    if lis[x]==mayor:
        cantidad=cantidad+1
if cantidad>1:
    print("El mayor se repite en la lista")