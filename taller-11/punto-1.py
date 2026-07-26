import datetime

def funcion():
    t = input()
    p = input()
    referencia = datetime.datetime.strptime(t, "%Y-%m-%d")
    vencimiento = datetime.datetime.strptime(p, "%Y-%m-%d")
    dif = referencia - vencimiento
    dias = dif.days
    mes = dif.days // 30
    horas = dif.days * 24
    minutos = dif.days * 24 * 60
    segundos = dif.days * 24 * 60 * 60
    if dias >= 30:
        print(f"Vencida: mes(es): {mes}, horas: {horas}, minutos: {minutos}, segundos: {segundos}")
    elif dias < 1:
            print(f"A tiempo: vence en {dias*(-1)} dias")
    elif dias < 30:
        print(f"Vencida: dias: {dias}, horas: {horas}, minutos: {minutos}, segundos: {segundos}")
    
x = int(input())
for i in range(x):
    funcion()