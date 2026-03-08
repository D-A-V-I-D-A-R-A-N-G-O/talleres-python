x = int(input())
def funcionTramos(x):
    for i in range(x):
        x = int(input())
        if x >= 2:
            y = x+3
        else:
            y = x**2-(7*x)+5
        print(y)
        
funcionTramos(x)