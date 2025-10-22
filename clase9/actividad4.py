#Crear una función que reciba una lista de enteros y devuelva el producto de todos los números.
def productoValores(lista):
    acumulador = 1

    for x in range(len(lista)):
        acumulador = acumulador * lista[x]

    return acumulador

lista = [5, 10, 2, 3, 4]

resultadoProducto = productoValores(lista)

print("El producto de", lista, "=", resultadoProducto)