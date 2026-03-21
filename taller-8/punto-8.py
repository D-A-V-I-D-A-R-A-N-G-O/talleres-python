numero = int(input())
contador_interno = int((numero-4)/2)
contador_externo = 0
for i in range(numero):
    if i+1 == numero/2 or i+1 == numero/2+1:
        print("*"*numero)
    elif i+1 == numero/2-1 or i+1 == numero/2+2:
        p = int((numero-4)/2)
        print(" "*p + "****")
    elif i < int(numero/2-2):
        print("*"+" "*contador_interno+ "**" + " "*contador_interno +"*")
    elif i > int(numero/2):
        print("*"+" "*contador_interno+ "**" + " "*contador_interno +"*")
