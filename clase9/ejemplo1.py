def menor(lista):
    menor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor

lista = [1, 2, 3, 4, 5]
print(menor(lista))

lista = [5, 4, 3, 2, 10]
print(menor(lista))