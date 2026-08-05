from datetime import timedelta

n = int(input())

for i in range(n):
    lista = input().split()
    
    salida1 = timedelta(hours=((int(lista[0][0]))*10+int(lista[0][1])), minutes=((int(lista[0][3]))*10+int(lista[0][4])))
    llegada1 = timedelta(hours=((int(lista[1][0]))*10+int(lista[1][1])), minutes=((int(lista[1][3]))*10+int(lista[1][4])))
    salida2 = timedelta(hours=((int(lista[2][0]))*10+int(lista[2][1])), minutes=((int(lista[2][3]))*10+int(lista[2][4])))
    llegada2 = timedelta(hours=((int(lista[3][0]))*10+int(lista[3][1])), minutes=((int(lista[3][3]))*10+int(lista[3][4])))
    rango = timedelta(hours=((int(lista[4][0]))*10+int(lista[4][1])), minutes=((int(lista[4][3]))*10+int(lista[4][4])))
    vuelo1 = llegada1 - salida1
    vuelo2 = llegada2 - salida2
    entretiempo = salida2 - llegada1

    if vuelo1 < timedelta(0):
        vuelo1 += timedelta(hours=24)
    if vuelo2 < timedelta(0):
        vuelo2 += timedelta(hours=24)
    if entretiempo < timedelta(0):
        entretiempo += timedelta(hours=24)

    if rango <= entretiempo:
        r = "Si se puede"
    else:
        r = "No se puede" 
    
    vuelo1 = str(vuelo1)[:-3].zfill(5)
    vuelo2 = str(vuelo2)[:-3].zfill(5)
    entretiempo = str(entretiempo)[:-3].zfill(5)
    
    print(vuelo1, vuelo2, entretiempo, r)