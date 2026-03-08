x = int(input())
def fibonacci(x):
    a = 0
    b = 1
    c = 0
    impri = ""
    for i in range(x):
        c = a + b
        impri += str(a) + " "
        a = b
        b = c
    return impri

print(fibonacci(x))