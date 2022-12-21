num = int(input('Digite um número inteiro qualquer:'))
print('''Escolha uma das opçôes abaixo:
[ 1 ] CONVERTER PARA BINÁRIO
[ 2 ] CONVERTER PARA OCTAL
[ 3 ] CONVERTER PARA HEXADECIMAL''')
op = int(input('Digite sua opção:'))
if op == 1:
    print('O Valor de {} em Binário é {}.'.format(num,bin(num)[2:]))
elif op == 2 :
    print('O Valor de {} em Octal é {}.'.format(num,oct(num)[2:]))
elif op == 3:
    print('O Valor de {} em Hexadecimal é {}'.format(num,hex(num)[2:]))
else:
    print('Número Inválido. Tente novamente..')
