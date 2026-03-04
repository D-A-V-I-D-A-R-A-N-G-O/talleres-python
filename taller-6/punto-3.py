num_estudiantes = int(input())
examen = []
lista = []
iguales = 0
primer = 0
segundo = 0
for i in range(num_estudiantes):
    x = float(input())
    examen.append(x)
for i in range(num_estudiantes):
    x = float(input())
    if x == examen[i]:
        iguales += 1
        lista.append(0)
    elif x > examen[i]:
        segundo += 1
        lista.append(2)
    else:
        primer += 1
        lista.append(1)
x = 100/num_estudiantes
print(lista)
print("Gana 1:", round(x*primer, 1))
print("Gana 2:", round(x*segundo, 1))
print("Igual:", round(x*iguales, 1))