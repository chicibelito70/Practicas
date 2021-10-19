#Definir una lista que almacene por asignación los nombres de 5 personas. 
# Contar cuantos de esos nombres tienen 5 o más caracteres.


p=["Juan", "Maria","Julio", "San Miguel","Sofia"]
cant= 0
e=0
while e<len(p):
    if len (p[e])>=5:
        cant=cant+1
    e=e+1
print("Los nombres de la lista son: ",p)
print("La cantidad de caracteres en la lista son: ",cant)

