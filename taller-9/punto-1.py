numero = int(input())


def apellido(palabra):
    final = palabra[-2:]
    if final[1:] == "a":
        p = "Indio"
    elif final == "ix":
        p = "Galo"
    elif final == "us":
        p = "Romano"
    elif final == "ic":
        p = "Godo"
    elif final == "as":
        p = "Griego"
    elif final == "af":
        p = "Normando"
    elif final == "is" or final == "ax":
        p = "Breton"
    elif final == "ez":
        p = "Hispano"
    else:
        p = "Desconocido"
    return p


for i in range(numero):
    x = input()
    print(apellido(x))
