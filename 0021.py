#Confeccionar un programa que lea n pares de datos, cada par de datos corresponde 
# a la medida de la base y la altura de un triángulo. El programa deberá informar:
#a) De cada triángulo la medida de su base, su altura y su superficie.
#b) La cantidad de triángulos cuya superficie es mayor a 12.


n=int(input("Cuantos triángulos procesara: "))
cant=0
for x in range(n):
    base=int(input("ingrese un numero base :"))
    altura=int(input("ingrese un numero altura :"))
    super=base*altura/2
    print("--------------------------------")
    print("la superficie es: ",super)
    print("--------------------------------")
    if super>12:
        cant=cant+1
print("La cantidad de triangulos con superficie superior a 12 son",cant)
    