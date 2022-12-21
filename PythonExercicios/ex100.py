from random import randint
def random():
    pares = 0
    lista = []
    print('Sorteando 5 Valores...', end='')
    for c in range(0, 5):
        ale = randint(1, 10)
        lista.append(ale)
        print(f'{ale} ', end='')
        if ale % 2 == 0:
            pares += ale
    print('Pronto.')
    print(f'A soma dos valores pares: {lista} é de {pares}..')
print(random())

