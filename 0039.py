#Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. 3
# Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. 
# Mostrar esta tercer lista.
lis1=[]
for x in range(4):
    print("Carga de la primer lista")
    t=int(input("Ingrese un numero: "))
    lis1.append(t)
lis2=[]
for x in range(4):
    print("Carga de la segunda lista")
    e=int(input("Ingrese un numero: "))
    lis2.append(e)
listasuma=[]
for x in range(4):
    suma=lis1[x]+lis2[x]
    listasuma.append(suma)

print("Lista resultante: ",listasuma)
