#Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene como dato las
#  temperaturas medias mensuales de dichos paises.
#Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
#Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
#a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
#b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
#c - Calcular la temperatura media trimestral de cada país.
#c - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
#b - Imprimir el nombre del pais con la temperatura media trimestral mayor.

tempe=[]
prometemp=[]
paises=[]

for x in range(4):
    p=input("Ingrese el nombre de su pais: ")
    paises.append(p)
    temp1=int(input("Ingrese la primera temperatura de su pais: "))
    temp2=int(input("Ingrese la segunda temperatura de su pais: "))
    temp3=int(input("Ingrese la tercera temperatura de su pais: "))
    tempe.append([temp1,temp2,temp3])
print("Paises y temperaturas medias de los ultimos tres meses mensuales ")
for x in range(4):
    print(paises[x],tempe[x][0],tempe[x][1],tempe[x][2])
for x in range(4):
    pro=(tempe[x][0]+tempe[x][1]+tempe[x][2])//3
    prometemp.append(pro)

print("Paises y temperaturas medias trimestrales")
for x in range(4):
    print(paises[x],prometemp[x])

posmayor=0
for x in range(1,4):
    if prometemp[x]>prometemp[posmayor]:
        posmayor=x
print("Pais con temperatura media trimestral mayor:", paises[posmayor])