import math

def coseno(x, y):
    impri = ""
    variador = -1
    coseno = 1
    exponente = 2
    for i in range(x):
        impri += str(coseno) + ", "
        vari = variador * (y**exponente/math.factorial(exponente))
        coseno += vari
        exponente += 2
        variador = -1 * variador
        print(impri)
    return coseno


print(coseno(10, 1.0472))