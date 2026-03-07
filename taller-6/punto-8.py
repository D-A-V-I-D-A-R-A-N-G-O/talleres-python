lista_estudiantes = []
impares = []
pares = []
x = 0
while x >= 0:
    x = int(input())
    if x < 0:
        break
    lista_estudiantes.append(x)
    
for i in lista_estudiantes:
    if i % 2 == 0:
        pares.append(str(i))
    else:
        impares.append(str(i))
pares.sort()
impares.sort(reverse=True)
print(*pares, *impares)