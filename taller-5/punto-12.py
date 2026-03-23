filas  = int(input())
columnas = int(input())
f_pri= "\t"
for i in range(columnas):
    f_pri = f_pri + (str((i+1))+"\t")
print(f_pri)
print("")
for i in range(filas):
    p = str(i+1)
    c_pri = p + "\t"
    for p in range(columnas):
        c_pri = c_pri + (str(((p+1)*(i+1)))+"\t")
    print(c_pri)
