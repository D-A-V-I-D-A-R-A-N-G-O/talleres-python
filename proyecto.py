print("Adivina donde esta la reina de corazones")
opcion  = input("Seleccione jugar [J], tabla de posiciones [T], salir [S]:")
r = 0

def funcion_jugar():
    nombre = input("Por favor indique su nombre:")
    print(f"hola {nombre}, esta seccion aun esta en desarrollo")
    r = 0
    return r
  
def funcion_salir():
    print("Hasta luego")
    r = 1
    return r

def funcion_tabla():
    r = 1
    with open('tabla.txt', 'r', encoding='utf-8') as tabla:
        for linea in tabla:
            print(linea)

    print("pendiente de construccion")
    return r

while r == 0:
  match opcion:
    case "J":
        funcion_jugar
    case "T":
        funcion_tabla
    case "S":
        funcion_salir