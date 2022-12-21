from uteis import ex109u

p = float(input('Digite o preço: R$'))
print(f'A Metade de {ex109u.moeda(p)} é {ex109u.metade(p, formato=True)}')
print(f'O dobro de {ex109u.moeda(p)} é {ex109u.dobro(p, formato=True)}')
print(f'{ex109u.moeda(p)} mais 10% é {ex109u.aumentar(p, 10, formato=True)}')
print(f'{ex109u.moeda(p)} menos 13% é {ex109u.diminuir(p, 13, formato=True)}')

