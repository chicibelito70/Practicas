#Desarrollar una funcion que reciba un string como parametro y nos muestre la 
# cantidad de vocales. 
# Llamarla desde el bloque principal del programa 3 veces con string distintos.

def vocales(cadena):
    cant=0
    for x in range(len(cadena)):
        if cadena[x]=="a" or cadena[x]=="e" or cadena[x]=="i" or cadena[x]=="o" or cadena[x]=="u":
            cant=cant+1
    print("Cantidad de vocales de la palabra",cadena,"es",cant)
#principal
vocales("pedro")
vocales("juana no pudo ir al teatro hoy")
vocales("today is beatiful")