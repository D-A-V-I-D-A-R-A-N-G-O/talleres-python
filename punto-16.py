num = int(input())
numero = num
conta = 0
if num == 0:
    trans = "0"
else:
    trans = ""
while num >= 1:
    trans = str(num%2)+trans
    num = num//2
    conta += 1
print(f"El numero {numero} en binario es {trans}")
print(f"La conversion a binario se hizo en {conta} divisiones sucesivas")