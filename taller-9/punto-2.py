numero = int(input())


def el_modeludo(x):
    lista = x.split()
    la_mia = lista[0]
    lista.sort(reverse=True)
    if la_mia == lista[0]:
        es = "Estoy viajando en el vehiculo mas modeludo del camino"
    else:
        es = "Parece que hay otro vehiculo mas modeludo en el camino"
    return es


for i in range(numero):
    x = input()
    print(el_modeludo(x))
