longitud = int(input())
lista = []
delimitador = " "
conteo = 0
for i in range(longitud):
    x = input()
    lista.append(x.split(delimitador))

for i in lista:
    for e in i:
        if e == "0":
            conteo += 1
        else:
            continue
    if conteo == 2 or conteo == 1:
        es = "Si es la bandera de Escocia"
        conteo = 0
        continue
    else:
        es = "No es la bandera de Escocia"
        break
print(es)