#Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados
#  (4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar 
# los sueldos de los empleados agrupados en dos listas.
#Imprimir las dos listas de sueldos.


mn=[]
print("empresarios de la mañana")
print("----------------------------")
for x in range(4):
    m=float(input("Ingrese su sueldo:   "))
    mn.append(m)
print("----------------------------")
tr=[]
print("empresarios de la tarde ")
print("----------------------------")
for x in range(4):
    t=float(input("Ingrese su sueldo:   "))
    tr.append(t)
print("----------------------------")
print("el turno de la  manañana es: ",mn)
print("----------------------------")
print("el turno de la  tarde es: ",tr)

