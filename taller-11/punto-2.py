import datetime
x = int(input())

for i in range(x):
    r = input()
    fecha = datetime.datetime.strptime(r, "%Y-%m-%d %H:%M:%S")
    dia = fecha.isoweekday()
    hora = int(datetime.datetime.strftime(fecha, "%H%M"))
    if dia == 2:
        d = "Martes"
        if (hora >= 0 and hora <= 459) or (hora >= 2300 and hora <= 2359):
            engagament = "Engagement medio bajo"
        elif (hora >= 500 and hora <= 659) or (hora >= 1600 and hora <= 2359):
            engagament = "Engagement medio"
        elif (hora >= 700 and hora <= 759) or (hora >= 1400 and hora <= 1559):
            engagament = "Engagement medio alto"
        elif (hora >= 800 and hora <= 1360):
            engagament = "Engagement alto"
        else:
            engagament = "No "
    else:
        d = "Otro dia"
        if (hora >= 0 and hora <= 459) or (hora >= 2300 and hora <= 2359):
            engagament = "Engagement bajo"
        else:
            engagament = "Sin informacion"
    print(f"{d}: {engagament}")