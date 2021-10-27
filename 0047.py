#Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
# Desde el bloque principal del programa 
# llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)

def menor():
    t=int(input("Ingrese un valor: "))
    e=int(input("Ingrese un valor: "))
    w=int(input("Ingrese un valor: "))
    if t<e and t<w:
        print(t)
    else:
        if e<w:
            print(e)
        else: 
            print(w)

#principal

menor()
menor()