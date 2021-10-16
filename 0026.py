#Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron.
#  Tener en cuenta que un espacio en blanco es igual a
#" ", en cambio una cadena vacía es ""


n=input("Ingrese una oracion: ")
cant=0
x=0
while x <len(n):
    if n[x]==" ":
        cant=cant+1
    x=x+1
print("La cantidad de espacios en blanco ingresado son: ", cant)
