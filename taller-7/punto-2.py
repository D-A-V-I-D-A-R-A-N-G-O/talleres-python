def guay(x):
    p = 0
    y = 0
    sies = 0
    while p < x:
        y += 1
        p += y
    if p == x:
        sies = 1
    return sies
