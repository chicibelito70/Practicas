#Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. 
# Definir dos listas paralelas.
#  Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.

nom=[]
prec=[]

for x in range(5):
    print("-------------------------------------")
    n=input("Ingrese el nombre del producto: ")
    nom.append(n)
    print("-------------------------------------")
    p=int(input("Ingrese el precio del producto: "))
    prec.append(p)

cant=0
for x in range(1,5):
    if prec[x]>prec[0]:
        cant=cant+1
print("---------------------------------------------------------------------")
print("Cantidad de productos con un precio mayor al primer producto ingresado: ",cant)