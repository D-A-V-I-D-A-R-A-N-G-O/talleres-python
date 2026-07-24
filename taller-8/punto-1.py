def funcion(z):
    lista = []
    listaBien = []
    sinCambio = 0
    for i in range(z):
        x = float(input())
        lista.append(x)
        listaBien.append(x)
    listaBien.sort(reverse=True)
    for i in range(z):
        if listaBien[i] == lista[i]:
            sinCambio += 1
    return sinCambio

cuantos = int(input())

for i in range(cuantos):
    p = int(input())
    r = funcion(p)
    print(r)