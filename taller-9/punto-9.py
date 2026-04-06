expresiones_opositivas = ["por otro lado", "a pesar de", "en cambio", "mientras que", "no solo", "sin embargo"]
expresiones_causativas = ["hace que", "obligar a", "convencer a", "inducir a", "permitir que"]
conteo_causativas = 0
conteo_opositivas = 0
otro = []
delimite = " "
delimiter = "."
with open('discursos.txt', 'r', encoding='utf-8') as discurso:
    for linea in discurso:
        cc = 0
        co = 0
        texto = linea.lower().rstrip()
        for expresion in expresiones_causativas:
            cc += texto.count(expresion)
        for expresion in expresiones_opositivas:
            co += texto.count(expresion)
        print(f"Opositivos {co} Causativos {cc}")
