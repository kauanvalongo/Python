def dados(n):
    valido = False
    while not valido:
        p = str(input(n)).replace(',', '.').strip()
        if p.isalpha() or p == '':
            print(f'\033[0;30;41mERRO! O Valor "{p}" é Inválido, Digite Novamente...\033[m')
        else:
            valido = True
            return float(p)
