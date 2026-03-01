numcu = int(input())
lon = float(input())
pepe = int(1)
area = lon * lon
while numcu > pepe:
    lon = float(input())
    area = area + (lon * lon)
    
print(f"Ramon, el area total de la estructura basica del universo es de {area} centimetros cuadrados")