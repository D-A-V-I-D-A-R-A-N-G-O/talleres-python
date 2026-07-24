longitud = int(input())
lista = []

for i in range(longitud**2):
    x = int(input())
    lista.append(x)

prueba = lista[0]

for i in range(0, len(lista)-1, longitud):
    if lista[i] != prueba:
        x = "Matriz no escalar"
    else:
        x = "Matriz escalar"
    prueba = lista[i]
    lista.pop(i)
for i in lista:
    if i != 0:
        x = "Matriz no escalar"
        break

print(x)
