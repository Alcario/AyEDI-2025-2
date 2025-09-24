cantCoord = int(input("Ingrese la cantidad de coordenadas a verificar: "))

for i in range(cantCoord):
    x = int(input("x: "))
    y = int(input("y: "))

    if x>0 and y>0:
        print("Primer Cuadrante")
    elif x<0 and y>0:
        print("Segundo Cuadrante")
    elif x<0 and y<0:
        print("Tercer Cuadrante")
    elif x>0 and y<0:
        print("Cuarto Cuadrante")