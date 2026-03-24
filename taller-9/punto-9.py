expresiones_opositivas = ["por otro lado", "a pesar de", "en cambio", "mientras que", "no solo", "sin embargo"]
expresiones_causativas = ["hace que", "obligar a", "convencer a", "inducir a", "permitir que"]
otro = []
with open('discursos.txt', 'r', encoding='utf-8') as discurso:
    

for expresion in expresiones_causativas:
    conteo_causativas = otro.count(expresion)

for expresion in expresiones_opositivas:
    conteo_opositivas = otro.count(expresion)

print(f"Opositivos {conteo_opositivas} Causativos {conteo_causativas}")