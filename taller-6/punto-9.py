longitud = int(input())
mediana = float()
lista = []
for i in range(longitud):
    x = int(input())
    lista.append(x)
lista.sort()
if longitud%2 == 0:
    x = longitud/2-1
    x1 = longitud/2
    mediana = float((lista[int(x1)] + lista[int(x)])/2)
else:
    x = longitud/2-0.5
    mediana = float(lista[int(x)])
print(round(mediana, 1))