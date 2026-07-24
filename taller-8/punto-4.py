import math

def funcion(x, y):
    lista_cos = ""
    variador = -1
    exponente = 2
    cos_valor = 0
    r = 1

    for i in range(x):
        cos_valor += r
        if i != x-1:
            lista_cos += str(round(r, 2)) + ", "
        else:
            lista_cos += str(round(r, 2))
        r = variador * (y ** exponente) / math.factorial(exponente)
        exponente += 2
        variador *= -1

    print(lista_cos)
    print(round(cos_valor, 2))

x = int(input())
y = float(input())

funcion(x, y)