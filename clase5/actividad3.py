valoresEnteros = []

for i in range(5):
    valorIngresado = int(input("Ingrese un valor entero "))
    valoresEnteros.append(valorIngresado)

for i in range(5):
    if (valoresEnteros[i]%2) == 0:
        #Mostrando los valores pares de la lista
        print("Valor par: ", valoresEnteros[i])

print(valoresEnteros)