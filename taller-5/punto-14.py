alt = float(input())
rebote = 0
while alt >= 0.5:
    rebote += 1
    alt = alt * (2/3)
    print(f"Rebote: {rebote}, altura actual: {alt}")
print(f"Se necesitaron {rebote} rebotes para alcanzar altura inferior a 0.5")