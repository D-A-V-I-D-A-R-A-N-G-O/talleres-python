tabla = []
longitud = int(input())
for i in range(longitud):
    tabla.append([])

for i in range(longitud):
    for e in range(longitud):
        x = int(input())
        tabla[i].append(x)
print("termino la incersion de datos")

for e in range(longitud):
    for o in range(1, longitud):
        for i in tabla[e][:o:-1]:
            print(i)

print(tabla)