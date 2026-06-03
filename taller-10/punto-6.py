filas = int(input())
columnas = int(input())
r = 1
mayor = 0
menor = 100
el_mayor = 0
el_menor = 0

for i in range(filas):
    print(mayor)
    print(menor)
    print("iteracion",i)
    for j in range(columnas):
        x = int(input())
        r = r * x
    print("erre es", r)
    
    if r > mayor:
        mayor = i
    if r < menor:
        menor = i
    print("mayor es", mayor)
    print("menor es", menor)
    r =  1

print(mayor)
print(menor)