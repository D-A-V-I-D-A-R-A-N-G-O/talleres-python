tabla = [[1, 2, 3], [0, 4, 5], [0, 0, 7]]
longitud = 3

superior = []
inferior = []

final = longitud - 1 

for i in tabla:
    for e in i[:final:]:
        superior.append(e)
        final -= 1


final = 0
for i in tabla[::-1]:
    for e in i[::-1][final:]:
        inferior.append(e)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        final += 1

print(superior)
print(inferior)
