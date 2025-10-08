#Ingresar 4 nombres y mostrarlos en orden alfabético
nombres = []

for i in range(4):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
print(nombres)
nombres.sort()
print(nombres)