#Confeccionar una función que reciba tres enteros y 
# los muestre ordenados de menor a mayor. En otra función solicitar la carga de 3 
# enteros por teclado y proceder a llamar a la primer función definida.

def ordenador(v1,v2,v3):
    if v1<v2 and v1<v3:
        if (v2<v3):
            print(v1,v2,v3)
        else:
            print(v1,v3,v2)
    else:
        if (v2<v3):
            if (v1<v3):
                print(v2,v1,v3)
            else:
                print(v2,v3,v1)
        else:
            if (v1<v2):
                print(v3,v1,v2)
            else:
                print(v3,v2,v1)

def lacarga():
    n=int(input("Ingrese un numero: "))
    t=int(input("Ingrese un numero: "))
    y=int(input("Ingrese un numero: "))
    ordenador(n,t,y)

#principal
lacarga()

