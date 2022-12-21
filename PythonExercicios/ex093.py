ficha = {}
gols = []
total = 0
ficha['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidass ele jogou? :'))
for c in range(0,partidas):
    ficha['gols'] = int(input(f'Quantos Gols o {ficha["nome"]} fez na {c}. Partida?'))
    gols.append(ficha['gols'])
    total += ficha['gols']
ficha['gols'] = gols
ficha['total'] = total
print('=='*30)
print(ficha)
print('=='*30)
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}')
print('=='*30)
for i, v in enumerate(ficha['gols']):
    print(f'   => Na Partida {i}, Fez {v} Gols.')
