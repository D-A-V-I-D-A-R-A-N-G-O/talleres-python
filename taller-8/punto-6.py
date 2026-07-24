def barras(x):
    impares = 0
    pares = 0
    codigo = list(str(x))
    for i in codigo[(len(codigo)-2)::-2]:
        impares += int(i)*3
    for i in codigo[(len(codigo)-3)::-2]:
        pares += int(i)
    suma = impares + pares
    resto = (10 - (suma % 10)) % 10
    if resto == int(codigo[(len(codigo)-1)]):
        print("CORRECTO")
    else:
        print("INCORRECTO")    
    

while True:
    x = int(input())
    if x >= 0:
        barras(x)
    else:
        break