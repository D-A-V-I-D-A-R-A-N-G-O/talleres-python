numero = int(input())
c_i = int((numero-4)/2)
c_e = 0
c_i2 = 0
c_e2 = int((numero-4)/2)
for i in range(numero):
    if i+1 == numero/2 or i+1 == numero/2+1:
        print("*"*numero)
    elif i+1 == numero/2-1 or i+1 == numero/2+1:
        p = int((numero-4)/2)
        print(" "*p + "****")
    elif i < int(numero/2-2):
        print(" "*c_e + "*" + " "*c_i + "**" + " " *c_i + "*")
        c_i -= 1
        c_e += 1
    elif i > int(numero/2):
        print(" "*c_e2 + "*" + " "*c_i2 + "**" + " " *c_i2 + "*")
        c_i2 += 1
        c_e2 -= 1
