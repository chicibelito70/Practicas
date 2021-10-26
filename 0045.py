#Crear una lista de 5 enteros y cargarlos por teclado. 
# Borrar los elementos mayores o iguales a 10 y generar una nueva lista 
# con dichos valores
lis=[]
for x in range(5):
    e=int(input("Ingrese un valor: "))
    lis.append(e)
print("Lista original: ",lis)

lista=[]
pos=0
while pos<len(lis):
    if lis[pos]>=10:
        lista.append(lis.pop(pos))
    else:
        pos=pos+1
print("Lista despues de borrar los elementos mayores o iguales a 10: ",lis)
print("----------------------------------------------------------------------")
print("Lista generada con los elementos mayores o iguales a 10: ",lista)

