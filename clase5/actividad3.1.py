valoresEnteros = []

for i in range(5):
    valorIngresado = int(input("Ingrese un valor entero "))
    valoresEnteros.append(valorIngresado)

    #1º forma para comparar si el valor ingresado es par o impar
    #(Con variables simples)
    #if (valorIngresado%2) == 0:
        #Mostrando los valores pares de la lista
    #    print("Valor par: ", valoresEnteros[i])

    #2º forma de saber si el valor ingresado es par o impar
    # (listas)
    if (valoresEnteros[i]%2) == 0:
        print("Valor par: ", valoresEnteros[i])
print(valoresEnteros)