numero = int(input())


def circulo(x):
    lista = x.split()
    ff = lista.count("FF")
    mm = lista.count("MM")
    if ff != mm:
        r = "Circulo imposible"
    else:
        r = "Circulo de cables "
    return r


for i in range(numero):
    x = input()
    print(circulo(x))
