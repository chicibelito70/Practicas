#Definir una lista por asignación con 5 enteros. 
# Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.


p=[10,20,15,30,18,4]
cant= 0
t=0
while t<len(p):
    if p[t]>=7:
        cant=cant+1
    t=t+1
print("La lista esta constituida por los elementos: ",p)
print("La cantidad de valores mayores a 7 en la lista son: ",cant)


