num_partidas = int(input())
minimo = int(input())
maximo = int(input())
lista = []
for i in range(0, num_partidas):
    x = int(input())
    lista.append(x)

for i in range(minimo, maximo+1):
    contador = 0
    for e in range(len(lista)):
        if i == lista[e]:
            contador += 1
    print(f"{i}: {contador}")