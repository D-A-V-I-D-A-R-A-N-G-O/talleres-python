import math
def sigmoide(x):
    r = 1/(1 + math.exp(-x))
    return round(r, 10)