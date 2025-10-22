#Definir una función que reciba una lista de enteros y un número entero, y muestre cada elemento multiplicado por ese valor.
def tablaMultiplicacion(lista, numero):
    print("-----------------------------")
    print("Tabla del", numero, ":\n")
    for x in range(len(lista)):
        print(lista[x], "x", numero, "=", (lista[x]*numero))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero = 2

tablaMultiplicacion(lista, numero)
print("-----------------------------")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero = 3

tablaMultiplicacion(lista, numero)