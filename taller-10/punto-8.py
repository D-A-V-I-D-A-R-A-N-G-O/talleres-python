num_palabras = int(input())
diccionario = {}

for i in range(num_palabras):
    x = input()
    lista = x.split(":")
    diccionario[lista[0]] = lista[1]

num_oraciones = int(input())
traducido = ""
for i in range(num_oraciones):
    x = input()
    oracion = x.split(" ")
    for e in oracion:
        traducido += diccionario[e] + " "
    print(traducido)
    traducido = ""