import datetime

n = int(input())

for i in range(n):
    horas = input().split()
    h_inicio = datetime.datetime.strptime(horas[0], "%H:%M:%S")
    h_fin = datetime.datetime.strptime(horas[1], "%H:%M:%S")
    
    if h_fin <= h_inicio:
        h_fin += datetime.timedelta(days=1)
    
    datos = input().split()
    t = int(datos[0])
    c = int(datos[1])
    
    tiempo_total = h_fin - h_inicio
    intervalo = tiempo_total / (t - 1)
    resultado = h_inicio + intervalo * (c - 1)
    print(resultado.strftime("%H:%M:%S"))