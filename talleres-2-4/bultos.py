maxkg = float(input())
bulto = int(input())

p = int(0)
pesoaco = float(0)

while p <= bulto:
    peso = float(input())
    if pesoaco + peso > maxkg:
        break
    pesoaco += peso
    p += 1

print(f"Caben {p} bultos de papa")