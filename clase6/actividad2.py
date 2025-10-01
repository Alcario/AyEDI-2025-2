#Altura, edad y nombre de dos personas, demostrar quien es la más alta
#Datos de la primera persona
print("--------------------------------------\n\tDATOS DE LA PRIMERA PERSONA\n--------------------------------------")
altura1 = float(input("Ingrese la altura: "))
edad1 = int(input("Ingrese la edad: "))
nombre1 = input("Ingrese el nombre: ")

#Datos de la segunda persona
print("\n\n--------------------------------------\n\tDATOS DE LA SEGUNDA PERSONA\n--------------------------------------")
altura2 = float(input("Ingrese la altura: "))
edad2 = int(input("Ingrese la edad: "))
nombre2 = input("Ingrese el nombre: ")

if altura1>altura2: 
    print(nombre1, "es más alto/a que", nombre2)
else:
    print(nombre2, "es más alto/a que", nombre1)