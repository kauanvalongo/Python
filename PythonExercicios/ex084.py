lista = []
dados = []
pesado = 0
leve = 0
while True:
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(float(input('Digite o peso da pessoa: ')))
    if len(lista) == 0:
        pesado = dados[1]
        leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    lista.append(dados[:])
    dados.clear()
    cont = str(input('Quer Continuar? [S/N]'))
    if cont in 'Nn':
        break
print('-='*30)
print(f'Ao todo foram cadastradas {len(lista)} pessoas.')
print(f'A pessoa mais pesada pesa: {pesado}Kg e se chama:',end=' ')
for p in lista:
    if p[1] == pesado:
        print(f'[{p[0]}]', end='-')
print(f'\nA pessoa mais leve pesa {leve}Kg e seu nome é: ')
for p in lista:
    if p[1] == leve:
        print(f'[{p[0]}]', end='-')
