num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou os números : {num}')
print(f'\nO valor 9 apareceu {num.count(9)} vezes ')
if 3 in num:
    print(f'A posição do numero 3 é encontrado pela primeira vez na {num.index(3) + 1} posição')
else:
    print('O número [3] não foi digitado')
print('Os números pares são: ')
for c in num:
      if c % 2 == 0:
          print(f'{c}', end='-')

print('cabô')

