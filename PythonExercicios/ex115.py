from uteis import ex115

arq ='cursoemvideo.txt'

if not ex115.arquivoexiste(arq):
    ex115.criaraquivo(arq)

while True:
    print('-'*40)
    print(f'{"MENU PRINCIPAL".center(40)}')
    print('-'*40)
    print('\033[33m1\033[m - \033[36mVer Pessoas Cadastradas\033[m')
    print('\033[33m2\033[m - \033[36mCadastrar Novas Pessoas\033[m')
    print('\033[33m3\033[m - \033[36mSair do Sistema\033[m')
    print('-'*40)
    verdade = False
    resp = str(input('\033[34mSua Opção:\033[m '))
    while True:
        if not resp.isnumeric():
            print('\033[0;30;41mERRO! Digite Um Número Válido!\033[m')
            resp = str(input('\033[34mSua Opção:\033[m '))
        else:
            break
    if int(resp) == 3:
        print('-' * 40)
        print(f'{"SAINDO DO SISTEMA... ATÉ LOGO!".center(40)}')
        print('-' * 40)
        break
    v = False
    while not v:
        try:
            if int(resp) == 1:
                print('-' * 40)
                print(f'{"PESSOAS CADASTRADAS".center(40)}')
                print('-' * 40)
                ex115.lerarquivo(arq)
                v = True
            elif int(resp) == 2:
                print('-' * 40)
                print(f'{"NOVO CADASTRO".center(40)}')
                print('-' * 40)
                nome = str(input('Nome: '))
                idade = ex115.leiaint('Idade: ')
                ex115.cadastrar(arq, nome, idade)
                v = True
            else:
                print(f'\033[0;30;41mERRO! DIGITE A BOSTA DE UM NÚMERO VÁLIDO.\033[m')
                v = True
        except (TypeError, ValueError, KeyboardInterrupt):
            print(f'\033[0;30;41mERRO! DIGITE A BOSTA DE UM NÚMERO VÁLIDO.\033[m')
            v = True