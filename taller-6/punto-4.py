num_notas = int(input())
lista_notas = []
mayor = ""
menor = ""
for i in range(num_notas):
    x = float(input())
    lista_notas.append(x)
promedio = round(sum(lista_notas)/len(lista_notas), 1)
for e in range(num_notas):
    if lista_notas[e] > promedio:
        mayor += str(lista_notas[e]) + " "
    else:
        menor += str(lista_notas[e]) + " "
print(mayor)
print(menor)