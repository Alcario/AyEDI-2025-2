#Crear una función que reciba una lista de palabras y devuelva la palabra con más letras.
def palabraMasLarga(palabra1, palabra2):
    longitud1 = len(palabra1)
    longitud2 = len(palabra2)

    if longitud1>longitud2:
        return palabra1
    elif longitud2>longitud1:
        return palabra2
    else:
        return -1
    
ejemplo1 = palabraMasLarga("Pepito", "Luciana")
print("La palabra más larga es: ", ejemplo1)

ejemplo1 = palabraMasLarga("Luciano", "Luciana")
if ejemplo1 == -1:
    print("Ambas palabras son iguales")
else:
    print("La palabra más larga es: ", ejemplo1)