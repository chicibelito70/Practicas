#Crear una lista de enteros por asignación. Definir una función que reciba una 
# lista de enteros y un segundo parámetro de tipo entero. Dentro de la función 
# mostrar cada elemento de la lista multiplicado por el valor entero enviado.
#lista=[3, 7, 8, 10, 2]
#multiplicar(lista,3)


def mult(lis, entero):
    for x in range(len(lis)):
        mut=lis[x]*entero
    print(mut)

#principal
lista=[3, 7, 8, 10, 2]
print("Lista original:",lista)
print("Lista multiplicando cada elemento por 3")
mult(lista,3)