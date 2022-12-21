def leiaint(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[0;30;41mERRO! O VALOR DIGITADO É INVÁLIDO.\033[m')
        except (KeyboardInterrupt):
            print('\033[0;30;41mERRO! O Usuário Não Digitou Nenhum Valor\033[m')
            return 0
        else:
            return n


def leiafloat(num):
    while True:
        try:
            n = float(input(num))
        except (TypeError, ValueError):
            print('\033[0;30;41mERRO! O VALOR DIGITADO É INVÁLIDO\033[m')
        except (KeyboardInterrupt):
            print('\033[0;30;41mO USUÁRIO NÃO DIGITOU NENHUM VALOR..')
            return 0
        else:
            return n

n1 = leiaint('Digite um Número Inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real digitado foi {n2}')
