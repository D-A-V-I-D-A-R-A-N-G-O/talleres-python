def funcion(x):
    lista = list(range(1,x+1))
    lista1 = []
    while 1 < len(lista):
        if len(lista) == 2:
            lista1.append(str(lista[0]))
        else:
            lista1.append(str(lista[0])+",")            
        lista.pop(0)
        lista.append(lista[0])
        lista.pop(0)
    print(*lista1)
    print(*lista)
x = 1
while x > 0:
    x = int(input())
    funcion(x)