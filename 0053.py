#Plantear una función que reciba un string en 
# mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'

def cantidad(palabra):
    cant=0
    for x in range(len(palabra)):
        if palabra[x]=='a' or palabra[x]=="A":
            cant=cant+1
    return cant


#principal

palabra=input("Ingrese una palabra: ")
print("La palabra",palabra,"tiene",cantidad(palabra),"a")