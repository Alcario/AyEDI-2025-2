#Mostrar 5 sumas de dos valores ingresados, reutilizando funciones.
def suma():
    valor1 = input("Ingrese un valor: ")
    valor2 = input("Ingrese un valor: ")

    print(valor1, "+", valor2, "=", (int(valor1)+int(valor2)))
    
for i in range(5):
    suma()