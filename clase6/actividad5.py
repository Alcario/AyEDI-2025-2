#Ingresar un nombre en minúsculas y decir si empieza con vocal.
nombre = input("Ingrese su nombre: ").lower()

acumulador = 0

if nombre[0] == "a":
    acumulador = 1
elif nombre[0] == "e":
    acumulador = 1
elif nombre[0] == "i":
    acumulador = 1
elif nombre[0] == "o":
    acumulador = 1
elif nombre[0] == "u":
    acumulador = 1

if acumulador>0:
    print("El nombre comienza por vocal")
else:
    print("El nombre comienza con consonante")