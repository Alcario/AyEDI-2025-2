#Cargar una lista con 5 números enteros y mostrar solo los que sean mayores a 10.
def mayorQue10(lista):
    print("Los valores de la lista mayores que 10 son: ")
    for x in range(len(lista)):
        if lista[x]>10:
            print(lista[x])

lista = [5, 11, 2, 50, 3]
mayorQue10(lista)