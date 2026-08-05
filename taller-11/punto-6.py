n = int(input())
def conversor(x):
    x = x.split(":")
    minutos = (int(x[0])*60)+int(x[1])
    return minutos

def funcion(x):
    tiempo = 0
    for i in range(0,len(x),2):
        diferencia = conversor(x[i+1])-conversor(x[i])
        tiempo += diferencia
    total = round((tiempo/720)*100,0)
    print(f"Porcentaje de tiempo libre: {100-total}%")

for i in range(n):
    r = input()
    lista = r.split(" ")
    funcion(lista)