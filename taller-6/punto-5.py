calculo = int(input())
algebra = int(input())
lista = []
lista1 = []
repetidos = ""
for i in range(calculo):
    x = int(input())
    lista.append(x)
for i in range(algebra):
    x = int(input())
    lista1.append(x)

for p in range(calculo):
    x = lista[p]
    for i in range(algebra):
        if x == lista1[i]:
            repetidos += str(lista1[i]) + " "

print(f"Los estudiantes que reprobaron ambas materias son: {repetidos}")