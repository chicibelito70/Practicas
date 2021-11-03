#Definir una lista de enteros por asignación en el bloque principal. Llamar a una función que reciba la lista y 
# nos retorne el producto de todos sus elementos. 
# Mostrar dicho producto en el bloque principal de nuestro programa.

def produ(lista):
    prod=1
    for x in range(len(lista)):
        prod=prod*lista[x]
    return prod
 
#principa
lista=[80, 2, 3, 4, 15]
print("Lista:", lista)
print("Multiplicacion de todos sus elementos:",produ(lista))
