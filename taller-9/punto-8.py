def trifelio(x):
    palabra1, palabra2 = x.split('-')
    palabra1 = list(palabra1)
    palabra2 = list(palabra2)
    palabra1.sort()
    palabra2.sort()
    
    if palabra1 == palabra2:
        return "Es trifelio"
    else:
        return "No es trifelio"


with open('trifelios.txt', 'r', encoding='utf-8') as trifelios:
    for linea in trifelios:
        print(trifelio(linea.strip()))
