num_estampitas = int(input())
estampitas = []
estampas = []
repetida = 0
for i in range(num_estampitas):
    x = int(input())
    estampitas.append(x)
for i in estampitas:
    if i not in estampas:
        estampas.append(i)
for i in estampas:
    for e in estampitas:
        if i == e:
            repetida += 1
    repetida -= 1
print(f"Carlitos debe intercambiar {repetida} estampitas para no tener repeticiones")