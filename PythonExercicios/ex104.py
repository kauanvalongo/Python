def leiaint(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! DIGITE UM NÚMERO VÁLIDO.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'O valor digitado foi {n}')