#Solicitar el lado de un cuadrado y preguntar si se desea calcular el perímetro o la superficie.
def calcular(opcion, lado):
    if (opcion == 1):
        print("Perimetro =", (lado*4))
    elif(opcion == 2):
        print("Superficie =", (lado**2))

while(True):
    print("Seleccione una opcion:")
    print("1) Perimetro")
    print("2) Superficie")
    print("3) Salir")

    opcion = int(input("-->"))

    if(opcion == 3):
        print("Hasta luego")
        break
    else:
        lado = int(input("Ingrese el valor del lado: "))
        calcular(opcion, lado)