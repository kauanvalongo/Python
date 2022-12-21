def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'O número {i} até o {f} de {p} em {p} fica:')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
        print('FIM!')

    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
        print('FIM!')


contador(1,10,1)
contador(10,0,2)
print()
print('-='*30)
print('Sua Vez de Escolher Os Fatores!')
ini = int(input('INÍCIO :'))
fim = int(input('FIM    :'))
pas = int(input('PASSO  :'))
contador(ini, fim, pas)
