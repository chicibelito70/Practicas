#Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas.
#  Contar la cantidad de vocales. Crear un segundo string con toda la oración en
#  minúsculas para que sea más fácil disponer la condición que verifica que es una vocal.

o=input("Ingrese una oracion:")
oracionmin=o.lower()
cant=0
x=0
while x<len(oracionmin):
    if oracionmin[x]=="a" or oracionmin[x]=="e" or oracionmin[x]=="i" or oracionmin[x]=="o" or oracionmin[x]=="u":
        cant=cant+1
    x=x+1
print("La cantidad de vocales de la oracion son: ",cant)