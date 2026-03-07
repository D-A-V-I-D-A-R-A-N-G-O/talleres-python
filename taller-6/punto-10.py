longi = int(input())
lista = []
lista1 = []
final = ""
for i in range(longi):
    x = int(input())
    lista.append(x)
for i in range(longi):
    x = int(input())
    lista1.append(x)

invertida = lista1[::-1]
for i in range(longi):
    final += str(lista[i]*invertida[i]) + " "
print(final)