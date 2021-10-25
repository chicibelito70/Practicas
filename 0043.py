#Desarrollar un programa que cree una lista de 50 elementos. 
#El primer elemento es una lista con un elemento entero, el segundo elemento 
# es una lista de dos elementos etc.
#La lista debería tener esta estructura y asignarle esos valores a medida que se crean 
# los elementos:
#[[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], etc....]
lista=[]
cant=1
for k in range(50):
    lista.append([])
    valor=1
    for x in range(cant):
        lista[k].append(valor)
        valor=valor+1
    cant=cant+1

print(lista)  