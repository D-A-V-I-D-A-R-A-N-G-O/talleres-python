def paresDivisibles(x, y):
    contador = 0
    for i in range(len(y)):
        for j in range(i+1, len(y)):
            print(y[i], y[j])
            if (y[i] + y[j]) % x == 0:
                contador += 1

    return contador