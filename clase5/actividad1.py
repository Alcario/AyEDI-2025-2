listaEnteros = [7, 5, 3, 10, 4, 8]

acumulador = 0

for i in range(6):
    print(acumulador, "+", listaEnteros[i], "=", listaEnteros[i] + acumulador);
    acumulador = listaEnteros[i] + acumulador

print("-------------")
print("acumulador = ", acumulador)