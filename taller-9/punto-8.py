def trifelio(x):
    lista = x.split('-')
    parte1 = lista[0][:-2]
    parte2 = lista[0][-2:]
    palabra = parte2 + parte1

    if palabra == lista[1] or len(lista[0]) == 2:
        return "Es trifelio"
    else:
        return "No es trifelio"


with open('trifelios.txt', 'r', encoding='utf-8') as trifelios:
    for linea in trifelios:
        print(trifelio(linea.strip()))
