let1 = input()
num1 = float(input())
let2 = input()
num2 = float(input())
D=float()
T=float()
V=float()


if let1 == "D":
    num1 = D
elif let1 =="T":
    num1 = T
elif let1 =="V":
    num1 = V


if let2 == "D":
    num2 = D
elif let2 =="T":
    num2 = T
elif let2 =="V":
    num2 = V

if V!=0 and D!=0:
    print(f"T = {D/V}")
elif V!=0 and T!=0:
    print(f"D = {V*T}")
elif D!=0 and T!=0:
    print(f"V = {D/T}")