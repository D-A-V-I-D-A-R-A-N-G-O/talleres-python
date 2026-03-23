mensaje = open('mensaje.txt', 'r', encoding='utf-8')
lista = []
for linea in mensaje:
    lista.append(linea.strip())

mensaje.close()
for invertida in lista:
    if invertida != "":
        print(invertida[-1::-1])
