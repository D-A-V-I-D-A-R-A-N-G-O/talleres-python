filas = int(input())
columnas = int(input())
for i in range(filas):
    linea = str(i + 1)
    for c in range(columnas-1):
        linea += " " + str((i+1)**c)
    print(linea)