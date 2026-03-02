base = int(input())
miti = base//2
aste = "*"
for i in range(miti+1):
    print(aste*(i+1))
for i in range(miti, 0, -1):
    print(aste*(i))
