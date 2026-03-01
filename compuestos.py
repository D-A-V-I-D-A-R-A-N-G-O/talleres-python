numnum = int(input())
primo = 0
sumatoria = float(0)
divi = 0
for i in range(numnum):
    esprimo = True
    num = int(input())
    if num == 1:
        continue
    raiz = num**0.5
    for n in range(2, int(raiz) + 1):
        if num % n == 0:
            esprimo = False
            break
    if esprimo == False:
        sumatoria += num
        divi +=1
        continue
    else:
        primo += 1
print(round(sumatoria/divi, 1))