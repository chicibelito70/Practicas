#Confeccionar una función que calcule la superficie de un rectángulo y la retorne, 
# la función recibe como parámetros los valores de dos de sus lados:
#def retornar_superficie(lado1,lado2):
#En el bloque principal del programa cargar los lados de dos rectángulos 
# y luego mostrar cual de los dos tiene una superficie mayor.

def retornar_superficie(lado1,lado2):
    supe=lado1*lado2
    return supe
#principal
print("Primer rectangulo")
lado1=int(input("Ingrese un lado: "))
lado2=int(input("Ingrese un lado: "))
print("Segundo rectangulo")
lado3=int(input("Ingrese un lado: "))
lado4=int(input("Ingrese un lado: "))
if retornar_superficie(lado1,lado2)==retornar_superficie(lado3,lado4):
    print("Los dos rectangulos tiene la misma superficie")
else:
    if retornar_superficie(lado1,lado2)>retornar_superficie(lado3,lado4):
        print("El primer rectangulo tiene una superficie mayor")
    else:
        print("El segundo rectangulo tiene una superficie mayor")
    