time = []
ficha = {}
gols = []
while True:
    ficha.clear()
    ficha['nome'] = str(input('Nome do jogador: '))
    tot = int(input('Quantas partidass ele jogou? :'))
    gols.clear()
    for c in range(0, tot):
        gols.append(int(input(f'Quantos Gols o {ficha["nome"]} fez na {c+1}. Partida?')))
        ficha['gols'] = gols[:]
    ficha['total'] = sum(gols)
    time.append(ficha.copy())
    while True:
        resp = str(input('Quer Continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N; ')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in ficha.keys():
    print(f'{i:<15} ', end='')
print()
print('--'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('=='*30)
while True:
    busca = int(input('Mostrar dados de qual jogador?'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe um jogador {busca}. ')
    else:
        print(f'-- Levantamento do Jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1}, Fez {g} Gols.')
    print('-='*40)
print('  <<< VOLTE SEMPRE! >>>  ')
