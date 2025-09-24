cantPares = 0
cont = 0
cantImpares = 0

while cont < 15:
    valorIngresado = int(input("Ingrese un numero entero: "))
    esPar = valorIngresado%2
    if esPar == 0:
        print("Valor ingresado par: ", valorIngresado)
    else:
        print("Valor Ingresado Impar: ", valorIngresado)
    cont = cont + 1


