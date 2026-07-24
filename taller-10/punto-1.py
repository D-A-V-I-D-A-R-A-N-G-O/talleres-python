longitud = int(input())
lista = []
for i in range(longitud**2):
    x = int(input())
    lista.append(x)

for i in range(0, len(lista)-1, longitud):
    if lista[i] != 1:
        x = "Matriz no identidad"
    else:
        x = "Matriz identidad"
    lista.pop(i) 
print(lista)
for i in lista:
    if i == 1:
        x = "Matriz no identidad"
        break

print(x)
