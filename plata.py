plata = int(input())

cincu = plata // 50000
restcincu = plata % 50000
venti = restcincu // 20000
restventi = restcincu % 20000
diez = restventi // 10000
restdiez = restventi % 10000
cin = restdiez // 5000
restcin = restdiez % 5000
dos = restcin // 2000
restdos = restcin % 2000
mil = restcin // 1000

if cincu > 0:
    print(f"{cincu} billetes de 50000")
if venti > 0:
    print(f"{venti} billetes de 20000")
if diez > 0:
    print(f"{diez} billetes de 10000")
if cin > 0:
    print(f"{cin} billetes de 5000")
if dos > 0:
    print(f"{dos} billetes de 2000")
if mil > 0:
    print(f"{mil} billetes de 1000")


