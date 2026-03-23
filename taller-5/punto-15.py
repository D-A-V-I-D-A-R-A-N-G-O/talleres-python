num = float(input())
x0 = num / 2
x = 0.5 * (x0 + (num/x0))
ite = 1
print(f"Iteracion {ite}, x_(n+1) = {x}, x_(n) = {x0}")
while abs(x - x0) > 10**-12:
    ite += 1
    x0 = x
    x = 0.5 * (x0 + (num/x0))
    print(f"Iteracion {ite}, x_(n+1) = {x}, x_(n) = {x0}")
print(f"La raiz cuadrada de {num} es {x} calculada en {ite} iteraciones")