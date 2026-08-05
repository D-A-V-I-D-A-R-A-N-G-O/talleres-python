import random

limiteSuperior = int(input())

random.seed(limiteSuperior)

maxval = random.randint(1, limiteSuperior)
print(f"Maximo: {maxval}")

contador = 0

# El ciclo se repite limiteSuperior - 1 veces
for _ in range(limiteSuperior - 1):
    # El valor aleatorio puede llegar hasta limiteSuperior (sin restarle 1)
    aleatorio = random.randint(1, limiteSuperior)
    
    if aleatorio > maxval:
        maxval = aleatorio
        contador += 1
        print(f"{aleatorio} <-- actualizado")
    else:
        print(aleatorio)

print(f"El valor maximo fue actualizado {contador} veces")