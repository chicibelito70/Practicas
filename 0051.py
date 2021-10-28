#Elaborar una función que nos retorne el perímetro 
# de un cuadrado pasando como parámetros el valor de un lado

def perimetro(lados):
    peri=lados*4
    return peri

#principal
lado=int(input("Ingrese el lado del cuadrado: "))
print("El perimetro es: ",perimetro(lado))