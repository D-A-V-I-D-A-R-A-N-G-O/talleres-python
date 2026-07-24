num_productos = int(input())
productos = {}

for i in range(num_productos):
    x = input()
    lista = x.split(":")
    nombre = lista[0]
    productos[nombre] = float(lista[1])

num_compras = int(input())
total = 0


for i in range(num_compras):
    x = input()
    lista = x.split(" ")
    nombre = lista[0]
    cantidad = int(lista[1])
    total += productos[nombre] * cantidad

if total > 100000:
    print(total * 0.7)
else:
    print(total)

