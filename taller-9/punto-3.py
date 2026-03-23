numero = int(input())


def panvocalica(x):
    if 'a' in x and 'e' in x and 'i' in x and 'o' in x and 'u' in x:
        r = "Panvocalica"
    else:
        r = "No panvocalica"
    return r


for i in range(numero):
    x = input()
    print(panvocalica(x))
