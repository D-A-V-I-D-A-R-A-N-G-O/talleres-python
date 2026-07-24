def funcion(m, n):
    if m == 0:
        r = n + 1
    elif m > 0 and n == 0:
        r = funcion(m-1, 1)
    elif m > 0 and n > 0:
        r = funcion(m-1, funcion(m, n-1))
    return r

x = int(input())
for i in range(x):
    m = int(input())
    n = int(input())
    print(funcion(m, n))