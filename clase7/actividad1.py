#Ingresar 5 números enteros y ordenarlos de menor a mayor

numeros = []

for i in range(5):
    n = int(input("Ingresar un numero: "))
    numeros.append(n)

print(numeros)

#Ordenamiento por méto de la burbuja 
#for i in range(4):
#    for j in range(4-i):
#        if numeros[j]>numeros[j+1]:
#            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

#Ordenamiento por sort (menor a mayor)
numeros.sort()

print(numeros)