def costos(x):
    lista = [x]
    dias = ["MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"]
    for i in range(5):
        x = float(input())
        lista.append(x)
    maximo = max(lista)
    minimo = min(lista)
    domingo = lista[5]
    promedio = round((sum(lista)/len(lista)), 2)
    if domingo == promedio or domingo < promedio:
        r = "NO"
    else:
        r = "SI"
    if maximo == minimo:
        print(f"EMPATE {r}")
    else:
        print(f"{dias[lista.index(maximo)]} {dias[lista.index(minimo)]} {r}")
            

while True:
    x = float(input())
    if x < 0:
        break
    costos(x)