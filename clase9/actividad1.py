#Crear una función que reciba una lista de números y muestre la suma total de sus elementos.

def sumaLista(lista):
    acumulador = 0

    for x in range(len(lista)):
        acumulador = acumulador + lista[x]
    
    print("La suma de la lista es:", acumulador)

lista = [5, 3, 8, 1, 3, 2]
sumaLista(lista)

lista = [5, 3, 8, 1, 3, 2, 10, 5]
sumaLista(lista)