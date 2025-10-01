#Ingresar un nombre en minúsculas y decir si empieza con vocal.
nombre = input("Ingrese su nombre: ").lower()

acumulador = 0

if nombre[0] in "aeiou":
    acumulador = 1

if acumulador>0:
    print("El nombre comienza por vocal")
else:
    print("El nombre comienza con consonante")