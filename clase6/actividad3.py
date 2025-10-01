acumulador = 0
opcion = "si"

while opcion == "si":
    numero = float(input("Ingrese un número: "))
    acumulador = acumulador + numero

    opcion = input("Ingresar no para salir o si para continuar: ")

print("El valor acumulado es: ", acumulador)