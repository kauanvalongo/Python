v1 = int(input('Digite um Valor:'))
v2 = int(input('Digite outro valor:'))
p = 0
while p != 5:
    p = int(input('''O que deseja fazer com esses números?
    [1] Somar
    [2] Multiplicar
    [3] Saber qual é maior
    [4] Digitar novos números
    [5] Terminar o Programa
    :'''))
    if p == 1:
        print(f'A soma dos números é: {v1 + v2}')
    if p == 2:
        print(f'A multiplicação dos números é: {v1 * v2}')
    if p == 3:
        if v1 > v2:
            print(f' o número {v1} é o maior')
        if v2 > v1:
            print(f'o número {v2} é maior')
        if v1 == v2:
            print('não há numero maior, os dois possuem o mesmo valor.')
    if p == 4:
        v1 = int(input('Digite um novo número:'))
        v2 = int(input('Digite o outro novo número:'))
        p = int(input('''O que deseja fazer com esses números?
    [1] Somar
    [2] Multiplicar
    [3] Saber qual é maior
    [4] Digitar novos números
    [5] Terminar o Programa
    :'''))
        if p == 1:
            print(f'A soma dos números é: {v1 + v2}')
        if p == 2:
            print(f'A multiplicação dos números é: {v1 * v2}')
        if p == 3:
            if v1 > v2:
                print(f' o número {v1} é o maior')
            if v2 > v1:
                print(f'o número {v2} é maior')
            if v1 == v2:
                print('não há numero maior, os dois possuem o mesmo valor.')

print('Programa Finalizado.')