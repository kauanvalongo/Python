from uteis import numeros
p = float(input('Digite o preço: R$'))
print(f'A Metade de {p} é {numeros.metade(p)}')
print(f'O dobro de {p} é {numeros.dobro(p)}')
print(f'{p} mais 10% é {numeros.aumentar(p, 10)}')
print(f'{p} menos 13% é {numeros.diminuir(p, 13)}')

