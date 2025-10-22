#Hacer una función que reciba tres enteros y muestre el menor.
def menorDeTres(entero1, entero2, entero3):
    if(entero1<entero2 and entero1<entero3):
        print("El menor valor es: ", entero1)
    elif (entero2<entero1 and entero2<entero3):
        print("El menor valor es:", entero2)
    elif (entero3<entero1 and entero3<entero2):
        print("El menor valor es:", entero3)
    elif (entero3==entero1 and entero3==entero2):
        print("Los tres valores son iguales")
    elif (entero1==entero2):
        print("Los valores 1 y 2 son iguales")
    elif (entero1==entero3):
        print("Los valores 1 y 3 son iguales")
    elif (entero2==entero3):
        print("Los valores 2 y 3 son iguales")

menorDeTres(4, 5, 8)
menorDeTres(6, 3, 2)
menorDeTres(6, 1, 7)
menorDeTres(3, 3, 3)
menorDeTres(3, 3, 1)
menorDeTres(3, 2, 3)
menorDeTres(3, 2, 2)