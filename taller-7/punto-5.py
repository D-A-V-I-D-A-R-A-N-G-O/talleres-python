def esPrimo(x):
    limite = int(x/2)
    lista = []
    for i in range(1, limite+1):
        if x % i == 0:
            lista.append(i)
    if sum(lista) == x:
        return True
    else:
        return False

x = int(input())
for i in range(x):
    x = int(input())
    if x < 0:
        print("El numero ingresado debe ser positivo")
    elif esPrimo(x) == True:
        print(f"El numero {x} es perfecto")
    else:
        print(f"El numero {x} no es perfecto")
