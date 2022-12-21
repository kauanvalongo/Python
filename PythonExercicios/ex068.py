import random
print('-=' * 20)
print('Jogue Par ou ímprar Comigo!')
while True:
    j = int(input('Digite Seu Número: '))
    pi = str(input('Par Ou Ímpar? [P/I] : '))
    c = random.randint(1,10)
    r = j + c
    n = (j + c) / 2
    print('-=' * 20)
    if pi in 'Pp':
        if n % 2 == 0:
            print(f'Eu joguei {c} e você jogou {j} o Resultado é {r} = [PAR]')
            print('Você ganhou!')
        else:
            print(f'Eu joguei {c} e você jogou {j} o Resultado é {r} = [ímpar]')
            print('Você Perdeu!')
            break
    if pi in 'Ii':
        if n % 2 != 0:
            print(f'Eu joguei {c} e você jogou {j} o Resultado é {r} = [ímpar]')
            print('Você ganhou!')
        else:
            print(f'Eu joguei {c} e você jogou {j} o Resultado é {r} = [PAR]')
            print('Você Perdeu!')
            break
