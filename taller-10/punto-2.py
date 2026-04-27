longitud = int(input())
lista = []
for i in range(longitud**2):
    x = int(input())
    lista.append(x)

for i in range(0, len(lista)-1, longitud):
    if lista[i] == 0:
        x = "Matriz no diagonal"
    else:
        x = "Matriz diagonal"
    lista.pop(i)
for i in lista:
    if i != 0:
        x = "Matriz no diagonal"
        break

print(x)
