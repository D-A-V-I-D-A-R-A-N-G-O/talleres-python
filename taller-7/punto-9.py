def funcion(x, y):
    if x == 0 and y == 0:
        r = 0
    elif x == 0:
        r = "Y"
    elif y == 0:
        r = "X"
    elif x > 0 and y > 0:
        r = 1
    elif x > 0 and y < 0:
        r = 4
    elif x < 0 and y < 0:
        r = 3
    elif x < 0 and y > 0:
        r = 2
    return r
x = int(input())
for i in range(x):
    x = float(input())
    y = float(input())
    print(funcion(x, y))
