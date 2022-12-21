ficha = {}
lista = []
media = 0
total = 0

while True:
    ficha.clear()
    ficha['nome'] = str(input('Nome: '))
    ficha['idade'] = int(input('Idade: '))
    while True:
        ficha['sexo'] = str(input('Sexo: [F/M]'))
        if ficha['sexo'] in 'MmFf':
            break
        else:
            print('Valor Inválido...')
    lista.append(ficha.copy())
    media += ficha['idade']
    while True:
        cont = str(input('Deseja continuar? [S/N]'))
        if cont in 'SsNn':
            break
        print('Erro! Digite S OU N.')
    if cont in 'Nn':
        break
print('=='*30)
print(f'A) O grupo tem {len(lista)} pessoas')
print(f'B) A média de idade do grupo é {media/len(lista)}')
print(f'C) As mulheres cadastradas foram : ', end='')
for m in lista:
    if m['sexo'] in 'Ff':
        print(f'{m["nome"]}', end = ', ')
print()
print(f'D) As pessoas acima da média são:')
for m in lista:
    if m['idade'] >= media/len(lista):
        print('   ', end='')
        for k, v in m.items():
            print(f'{k} = {v};', end='')
        print()
print(' <<< ENCERRADO >>> ')
