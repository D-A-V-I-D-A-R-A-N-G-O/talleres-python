def es_primo(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    raiz = int(num ** 0.5)
    for i in range(3, raiz + 1, 2):  # solo impares
        if num % i == 0:
            return False
    
    return True


cantidad = 0

numeros = [
2345678976544235435,
24578543263567453868,
879576968578786467846,
867856373457345756746799,
7475246245634151323,
642575474563465,
264586537463243,
46245878709756547,
76547432666874653421,
95764653435,
5462456898756543,
987654867,
543,
7654786475,
654746,
65346573451,
2456131,
22221111,
4236111,
1111
]

for n in numeros:
    if es_primo(n):
        cantidad += 1

print("Cantidad de primos:", cantidad)