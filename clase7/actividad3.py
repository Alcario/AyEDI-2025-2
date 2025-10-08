#Ingresar 3 alumnos y sus notas, ordenarlos por notas
alumnos = []
notas = []

for i in range(3):
    alumno = input("Ingrese el nombre del alumno: ")
    nota = int(input("Ingrese la nota del alumno "))

    alumnos.append(alumno)
    notas.append(nota)

print("Alumnos: ", alumnos)
print("Notas: ", notas)

for i in range(2):
    for j in range(2-i):
        if notas[j]>notas[j+1]:
            notas[j], notas[j+1] = notas[j+1],notas[j]
            alumnos[j], alumnos[j+1] = alumnos[j+1],alumnos[j]

print("Alumnos: ", alumnos)
print("Notas: ", notas)