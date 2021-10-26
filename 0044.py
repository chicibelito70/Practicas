#Crear dos listas paralelas. En la primera ingresar los nombres de empleados y 
# en la segunda 
# los sueldos de cada empleado.
#Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
#Borrar luego todos los empleados que tienen un sueldo mayor a 10000 
# (tanto el sueldo como su nombre)

empleados=[]
sueldo=[]
cant=int(input("Ingrese la cantidad de empleados: "))
for x in range(cant):
    nom=input("Ingrese su nombre: ")
    empleados.append(nom)
    sue=int(input("Ingrese su sueldo: "))
print("Estos son los empleados: ")
for x in range(len(sueldo)):
    print(empleados[x],sueldo[x])

posicion=0
while posicion<len(sueldo):
    if sueldo[posicion]>10000:
        sueldo.pop(posicion)
        empleados.pop(posicion)
    else:
        posicion=posicion+1

print("Listado de empleados que cobran 10000 o menos")
for x in range(len(sueldo)):
    print(empleados[x],sueldo[x])

