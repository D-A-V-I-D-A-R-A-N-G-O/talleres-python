import datetime

def formatear_diferencia(x):
    total_segundos = int(x.total_seconds())
    dias = total_segundos // 86400
    horas = (total_segundos % 86400) // 3600
    minutos = (total_segundos % 3600) // 60
    
    return f"{dias} dias, {horas} horas, {minutos} minutos"


n = int(input())
primero = input()
primero = datetime.datetime.strptime(primero, "%Y/%m/%d %H:%M")
segundo = primero
sumatoria = datetime.timedelta()
for i in range(n-1):
    x = input()
    referencia = datetime.datetime.strptime(x, "%Y/%m/%d %H:%M")
    diferencia = referencia - segundo
    sumatoria += diferencia
    print(formatear_diferencia(diferencia))
    segundo = referencia

promedio = sumatoria/(n-1)
print("Promedio:", formatear_diferencia(promedio))
    
    
