num = 0
while num >= 0:
    num = int(input())
    if num < 0:
        break
    preci = float(input())
    promo1 = round(num * preci * 0.7)
    promo2 = round(((num//3)*2*preci) + ((num%3)*preci)) 
    if promo1 > promo2 or promo1 == promo2:
        print(f"Mejor oferta 3x2: ${promo2}")
    else:
        print(f"Mejor oferta 30%: ${promo1}")