def circulo(x):
    lista = x.split()
    print(lista)
    for i in range(len(lista)-1):
        print(lista[i][-2:], lista[i+1][:2])
        if lista[i][-2:] == lista[i+1][:2] or lista[i][-3:] == lista[i+1][:3]:
            p = "Cadena completa"
            continue
        else:
            p = "Cadena rota"
            break
    return p


with open('palabras.txt', 'r', encoding='utf-8') as palabras:
    for linea in palabras:
        print(circulo(linea))
