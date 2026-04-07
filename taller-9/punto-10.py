binario = input()
lista1 = []
lista = []
resultado = 0

for i in range(len(str(binario))):
    lista.append(2**i)
lista.reverse()

for i in binario:
    lista1.append(int(i))

for i in range(len(binario)):
    resultado += (lista[i]*int(binario[i]))
    lista[i] = lista[i]*int(binario[i])

print(f"Digitos en binario: {lista1}")
print(f"Digito x Valor Posicional: {lista}")
print(f"Valor en decimal: {resultado}")
