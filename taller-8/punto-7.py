def productos():
    lista_productos = []
    lista_precios = []

    while True:
        x = float(input())
        if x < 0:
            break
        y = input()
        lista_precios.append(x)
        lista_productos.append(y)

    return lista_precios, lista_productos


def costo(lista_productos, lista_precios):
    domicilio_cantidad = []
    domicilio_producto = []
    total = 0

    while True:
        x = int(input())
        if x < 0:
            break
        y = input()
        domicilio_cantidad.append(x)
        domicilio_producto.append(y)

    for i in range(len(domicilio_cantidad)):
        precio = lista_precios[lista_productos.index(domicilio_producto[i])]
        total += precio * domicilio_cantidad[i]

    if len(domicilio_cantidad) == 1:
        total *= 1.10
    elif 2 <= len(domicilio_cantidad) <= 5:
        total *= 1.07
    elif 6 <= len(domicilio_cantidad) <= 10:
        total *= 1.05

    return round(total, 0)


cantidad = int(input())

for i in range(cantidad):
    lista_precios, lista_productos = productos()
    print(f"${costo(lista_productos, lista_precios)}")
