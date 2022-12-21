import random
from time import sleep
itens = ('Pedra' , 'Papel' , 'Tesoura')
c = random.randint(0,2)
print('Olá! Jogue Jokenpo Comigo!')
print('-=-' * 20)
str(print('''Os Números a Seguir Representarão as Jogadas:
[ 0 ] = Pedra
[ 1 ] = Papel
[ 2 ] = Tesoura'''))
j = int(input('Escolja a Sua jogada!'))
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!...')
sleep(1)
print('-=-' * 20)
print('Eu Joguei {}!'.format(itens[c]))
print('E Você Jogou {}!..'.format(itens[j]))
if c == 0:
    if j == 0:
        print('EMPATE!')
    elif j == 1:
        print('Você Ganhou!')
    elif j == 2:
        print('Você Perdeu!')
    else:
        print('Jogada Inválida')
if c == 1:
    if j == 0:
        print('Você Perdeu!')
    elif j == 1:
        print('EMPATE!')
    elif j == 2:
        print('Você Ganhou!')
    else:
        print('Jogada Inválida')
if c == 2:
    if j == 0:
        print('Você Ganhou!')
    elif j == 1:
        print('Você Perdeu!')
    elif j == 2:
        print('EMPATE!')
    else:
        print('Jogada Inválida')
