#En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo
#  a lo siguiente:
#a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
#b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, 
#colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y 
#colocar "Insuficiente" si la nota es inferior a 4.
#c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.

nom=[]
nota=[]

for x in range(4):
    n=input("Ingrese su nombre: ")
    nom.append(n)
    print("------------------------")
    no=int(input("Ingrese su nota: "))
    nota.append(no)
cant=0
for x in range(4):
    print(nom[x])
    print(nota[x])
    if nota[x]>8:
        print("Muy Bueno")
        cant=cant+1
    else:
        if nota[x]>=4:
            print("Bueno")
        else: 
            print("Insuficiente")
print("La cantidad de alumnos muy buenos son: ",cant)

