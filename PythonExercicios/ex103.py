def ficha(nome='desconhecido', gol=0):
    print(f'O jogador {nome} Fez {gol} gol(s) no campeonato.')


n = str(input('Qual o nome do jogador? :'))
g = str(input('Quantos gols ele fez no campeonato? :'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)