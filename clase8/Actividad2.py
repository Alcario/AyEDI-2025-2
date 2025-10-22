#Crear una función muestre el cuadrado de un número y otra el producto de dos números.
def mostrarCuadrado(numero):
    print("El cuadrado de", numero, "es:", numero**2)

def productoDosNumeros(numero1, numero2):
    print(numero1, "x", numero2, "=", numero1*numero2)

numero = int(input("Ingrese un numero: "))

mostrarCuadrado(numero)
productoDosNumeros(3, 4)