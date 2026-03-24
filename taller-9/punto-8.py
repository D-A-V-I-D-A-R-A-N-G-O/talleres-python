def trifelio(x):
    a, b = x.split('-')
    
    for i in range(1, len(a)):  # todas las divisiones posibles
        nueva = a[i:] + a[:i]
        if nueva == b:
            return "Es trifelio"
    
    return "No es trifelio"


with open('trifelios.txt', 'r', encoding='utf-8') as f:
    for linea in f:
        print(trifelio(linea.strip()))