#Definir por asignación una lista con 8 elementos enteros. 
# Contar cuantos de dichos valores almacenan un valor superior a 100

p=[100,200,300,400,500,600,700,800]
cant= 0
e=0
while e<len(p):
    if p[e]>=100:
        cant=cant+1
    e=e+1
print("La lista esta constituida por los elementos: ",p)
print("La cantidad de valores mayores a 100 en la lista son: ",cant)


