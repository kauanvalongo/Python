def cabecalho(msg):
    print('-'*42)
    print(f'{msg.center(42)}')
    print('-'*42)


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print('-'*42)
    opc = leiaint('\033[36mSua Opção: \033[m')
    return opc


def leiaint(n):
    while True:
        try:
            a = int(input(n))
        except(ValueError, TypeError):
            print('\033[0;30;41mERRO! Digite um Número Válido.\033[m')
        except(KeyboardInterrupt):
            print('\033[0;30;41mERRO! O USUÁRIO NÃO DIGITOU NADA.\033[m')
        else:
            return a


def arquivoexiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except(FileNotFoundError):
        return False
    else:
        return True


def criarq(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Problema ao Tentar Criar Arquivo..')
    else:
        print(f'Arquivo {arq} Criado com Sucesso')


def lerarq(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao tentar ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} Anos')
    finally:
        a.close()

def addarq(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de adicionar os registros. ')
        else:
            print(f'Os Registros de Nome e Idade de {nome} Foram Adicionados à Lista!')
            a.close()