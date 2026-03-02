n = int(input("number: "))

print(n//2)

for i in range((n//2)+1):
    print("*"(i+1))

for i in range((n//2), 0, -1):
    print("*"(i))
    