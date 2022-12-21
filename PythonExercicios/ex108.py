from uteis import ex108

p = float(input('Digite o preço: R$'))
print(f'A Metade de {ex108.moeda(p)} é {ex108.moeda(ex108.metade(p))}')
print(f'O dobro de {ex108.moeda(p)} é {ex108.moeda(ex108.dobro(p))}')
print(f'{ex108.moeda(p)} mais 10% é {ex108.moeda(ex108.aumentar(p, 10))}')
print(f'{ex108.moeda(p)} menos 13% é {ex108.moeda(ex108.diminuir(p, 13))}')

