#Un postulante a un empleo, realiza un test de capacitación,
#  se obtuvo la siguiente información: cantidad total de preguntas que se le realizaron y 
# la cantidad de preguntas que contestó correctamente. Se pide confeccionar un programa
#  que ingrese los dos datos por teclado e informe el nivel del mismo según el porcentaje
#  de respuestas correctas que ha obtenido, y sabiendo que:
	#Nivel máximo:	Porcentaje>=90%.
	#Nivel medio:	Porcentaje>=75% y <90%.
	#Nivel regular:	Porcentaje>=50% y <75%.
	#Fuera de nivel:	Porcentaje<50%.


t=int(input("ingrese numero de preguntas "))
c=int(input("ingrese numero de respuesta correctas "))
p=c*100/t
if p>=90:
    print("Nivel maximo")
else:
    if p>=75:
        print("Nivel medio")
    else:
        if p>=50:
            print("Nivel regular")
        else:
            print("Fuera de lugar")