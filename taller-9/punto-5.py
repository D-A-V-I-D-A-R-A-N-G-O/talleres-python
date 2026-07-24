numero = int(input())


def camelCase(x):
    lista = x.split('_')
    for i in range(1, len(lista)):
        lista[i] = lista[i].capitalize()
    delimitador = "".join(lista)
    return delimitador


for i in range(numero):
    x = input()
    print(camelCase(x))
