suma = 0

for i in range(10):
    x = int(input("Ingrese un número: "))
    
    if(i>=5):
        suma += x

print("El resultado de los últimos 5 valores es: ", suma)