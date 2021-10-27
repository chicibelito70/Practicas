#Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero 
# y muestre el cuadrado de dicho valor. La segunda que solicite la carga de dos valores 
# y muestre el producto de los mismos. 
# LLamar desde el bloque del programa principal a ambas funciones.

def cuadrado():
    n=int(input("Ingrese un numero entero: "))
    cuadrado=n*n
    print("El cuadrado del entero es: ",cuadrado)
def comentario():
    print("---------------------------------------")

def producto():
    t=int(input("Ingrese un numero entero: "))
    e=(input("Ingrese un numero entero: "))
    p=t*e
    print("el producto es: ",p)


#principal
cuadrado()
comentario()
producto()