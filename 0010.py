#Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y
#muestre un mensaje indicando si tiene 1, 2, o 3 cifras. 
#Mostrar un mensaje de error si el número de cifras es mayor.

n=int(input("Ingrese un valor:  "))

if n<=10:
     print("Tiene un dígito")
else:
    if n<=100:
        print("Tiene dos dígitos")
    else:
        if n<=1000:
            print("Tiene tres dígitos")
        else:
            print("Error en la entrada de datos.")

