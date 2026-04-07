letra = 65
numero = int(input())
patron = ["*"] * numero
print(patron)

for i in range(numero-1, -1, -1):
    impre = ""
    patron[i] = chr(letra)
    letra += 1
    impre = impre.join(patron)
    print(impre)
