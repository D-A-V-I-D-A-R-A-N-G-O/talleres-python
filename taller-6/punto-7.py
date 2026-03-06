num_dorsales = int(input())
dorsales = []
test = 1
dorsal_faltante = num_dorsales
for i in range(num_dorsales-1):
    x = int(input())
    dorsales.append(x)
dorsales.sort()
for i in dorsales:
    if i != test:
        dorsal_faltante = test
        break
    else:
        test += 1
        
print(f"La dorsal que falta es: {dorsal_faltante}")