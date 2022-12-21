palavras= ('aprender' , 'programar' , 'linguagem' , 'python')
for p in palavras:
    print(f'\n na palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in ('aeiou'):
            print(f'{letra}',end=' ')

