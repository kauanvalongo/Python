num = int(input('Digite um Número:'))
c = num
fator = 1
print(f'Calculando {num}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x 'if c > 1 else ' = ' , end='')
    fator *= c
    c -= 1
print(f'{fator}')