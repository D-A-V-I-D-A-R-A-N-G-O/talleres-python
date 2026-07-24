def narcisista(x):
    y = list(str(x))
    suma = 0
    for i in y:
        suma += int(i)**len(y)
    if suma == x:
        return 1
    else:
        return 0
