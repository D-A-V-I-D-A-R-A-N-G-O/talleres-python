tabla = []
longitud = int(input())
superior = []
inferior = []
for i in range(longitud):
    tabla.append([])
for i in range(longitud):
    for e in range(longitud):
        x = int(input())
        tabla[i].append(x)

final = 1
for i in tabla:
    for e in i[:final:]:
        inferior.append(e)
    final += 1
final = 0
for i in tabla:
    for e in i[final:]:
        superior.append(e)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    final += 1

for i in superior:
    if i == 0:
        es_supe = False
        break
    else:
        es_supe = True
        continue

for i in inferior:
    if i == 0:
        es_infe = False
        break
    else:
        es_infe = True
        continue
        
if es_supe and es_infe:
    print("No es triangular superior ni inferior")
elif es_supe and not es_infe:
    print("Triangular superior")
elif not es_supe and es_infe:
    print("Triangular inferior")