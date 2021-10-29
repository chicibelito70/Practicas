#Desarrollar una función que reciba una lista de string y nos retorne el que tiene 
# más caracteres. Si hay más de uno con dicha cantidad de caracteres debe retornar 
# el que tiene un valor de componente más baja.
#En el bloque principal iniciamos por asignación la lista de string:
#palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
#print("Palabra con mas caracteres:",mascaracteres(palabras))

def caracteres(palabras):
    posi=0
    for x in range(len(palabras)):
        if len(palabras[x])>=len(palabras[posi]):
            posi=x
    return palabras[posi]


#principal

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",caracteres(palabras))