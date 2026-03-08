def funcion(x):
    if x > 3:
        r = x**2 - 6*x + 4
    elif 3 >= x and x > -1:
        r = x**3 + 8
    elif x <= -1:
        r = (x+8)**0.5
    return round(float(r), 1)
def guncion(x):
    return round(float(3 - x), 1)
x = int(input())
print(funcion(guncion(x)))
print(guncion(funcion(x)))
print(funcion(funcion(x)))
print(guncion(guncion(x)))