import datetime
x = int(input())
pagina = input()
lista = []
sumas = datetime.timedelta(days=0)
diccionario = {}
diccionario1 = {}

for i in range(x):
    r = input()
    divi = r.split(".")
    sitio = divi[1]
    diccionario[sitio] = datetime.timedelta(days=0)
    diccionario1[sitio] = 0
    lista.append(r)

for i in lista:
    entrada = i.split(" ")
    sitio_web = entrada[3].split(".")
    inicio = datetime.datetime.strptime(entrada[1], "%H:%M:%S")
    fin = datetime.datetime.strptime(entrada[2], "%H:%M:%S")
    inicio = datetime.timedelta(hours=inicio.hour, minutes=inicio.minute, seconds=inicio.second)
    fin = datetime.timedelta(hours=fin.hour, minutes=fin.minute, seconds=fin.second)
    dif = fin - inicio
    diccionario[sitio_web[1]] += dif
    diccionario1[sitio_web[1]] += 1

promedio = diccionario[pagina]//diccionario1[pagina]
horas = promedio.seconds // 3600
minutos = (promedio.seconds%3600)//60
segundos = (promedio.seconds%3600)%60
print(f"{pagina}: {diccionario1[pagina]} veces, promedio: {horas} horas, {minutos} minutos, {segundos} segundos")
