from datetime import datetime

marzo28, marzo29 = 0, 0

def es_bisiesto(y: int) -> bool:
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

x = int(input())
for i in range(x):
    fecha = input()
    fecha = fecha.split(" ")
    inicio = datetime.strptime(fecha[0], "%d/%m/%Y")
    fin = datetime.strptime(fecha[1], "%d/%m/%Y")
    inicio = inicio.year
    fin = fin.year
    for año in range(inicio, fin + 1):
        if es_bisiesto(año):
            marzo28 += 1
        else:
            marzo29 += 1
    print(f"29 de marzo: {marzo29}")
    print(f"28 de marzo: {marzo28}")
    marzo29 = 0
    marzo28 = 0