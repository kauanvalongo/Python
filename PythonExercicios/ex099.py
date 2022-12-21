def maior(* num):
    cont = maio = 0
    print('Analisando os números...')
    for v in num:
        print(f'{v} ', end='')
        if cont == 0:
            maio = v
        else:
            if v > maio:
                maio = v
        cont += 1
    print(f'Foram informados {cont} números..')
    print(f'O maior número é {maio}')
    print('-=' * 30)

maior(1,5,3,5,8)
maior(2,4,1)
maior(92,56,23,12,3)
maior()
