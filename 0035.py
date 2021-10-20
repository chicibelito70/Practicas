#Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista.
#  Mostrar el nombre de persona menor en orden alfabético.

lis=[]
for x in range(5):
    t=input("Ingrese su nombre: ")
    lis.append(t)
nomn=lis[0]
for x in range(1,5):
    if lis[x]<nomn:
        nomn=lis[x]

print("La lista completa de nombres ingresado son: ",lis)
print("---------------------------------------------------")
print("El nombre menor en orden alfabetico es: ",nomn)
