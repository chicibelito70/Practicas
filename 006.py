#Se ingresan tres notas de un alumno, 
# si el promedio es mayor o igual a 70 mostrar un mensaje "Promocionado"

n=int(input("ingrese un numero:"    ))
e=int(input("ingrese un numero:"    ))
q=int(input("ingrese un numero:"    ))

r=(e+n+q)/3
if r>=70:
    print("En buena hora haz sido promovido con la nota:    ",r)
else:
    print("Malas noticias a sido reprobado :(, suerte para la proxima, tu nota es:  ",r)