#Definir una lista y almacenar los nombres de 3 empleados.
#Por otro lado definir otra lista y almacenar en cada elemento una sublista con 
#los números de días del mes que el empleado faltó.
#Imprimir los nombres de empleados y los días que faltó.
#Mostrar los empleados con la cantidad de inasistencias.
#Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días.
emple=[]
dias=[]

for k in range(3):
    n=input("Ingrese su nombre: ")
    emple.append(n)
    can=int(input("Ingrese los dias faltados: "))
    dias.append([])
    for x in range(can):
            dia=int(input("Ingrese el numero de dia que falto:"))
            dias[k].append(dia)
print("Nombres de empleados y dias que falto")
print("---------------------------------------")
for k in range(3):
    print(emple[k])
    for x in range(len(dias[k])):
         print(dias[k][x])
print("Nombres de empleados y cantidad de inasistencias")
for x in range(3):
    print(emple[x],len(dias[x]))

men=len(dias[0])
for x in range(1,3):
    if len(dias[x])<men:
        men=len(dias[x])

print("Empleado o empleados que faltaron menos")
for x in range(3):
    if len(dias[x])==men:
           print(emple[x])

