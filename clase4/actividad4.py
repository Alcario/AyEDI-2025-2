#cantidad de tríangulos
n = int(input("Ingrese la cantidad de tríangulos a controlar: "))

for i in range(n):
    lado1 = int(input("Ingrese el primer lado: "))
    lado2 = int(input("Ingrese el segundo lado: "))
    lado3 = int(input("Ingrese el tercero lado: "))

    if lado1 == lado2 and lado2 == lado3:
        print("El triángulo ingresado es equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("El triángulo ingresado es isoceles")
    else:
        print("El triángulo ingresado es escaleno")