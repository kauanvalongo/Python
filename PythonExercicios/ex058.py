import random
v = 0
c = random.randint(0,10)
print('O computador está pensando em um número entre 0 e 10.')
print('--=--' * 10)
j = int(input('Tente adivinhar o número que o computador está pensando!:'))
while j != c:
    j = int(input('Você errou! Tente novamente:'))
    v += 1
print(f'Você Finalmente Acertou! O computador estava pensando em {c}!')
print(f'Tentativas totais = {v}')
