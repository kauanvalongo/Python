def cabeca(msg):
    print('-'*42)
    print(f'{msg.center(42)}')
    print('-' * 42)


def menu(lista):
    cabeca('MENU PRINCIPAL')
    c = 1
    for c in range(0, len(lista)):
        print(f'\033[33m{c+1}\033[m - \033[34m{lista[c]}\033[m')
        c+=1
    print('-' * 42)
    resp = leiaint('\033[36mSua Opção: \033[m')
    return resp

def leiaint(n):
    while True:
        try:
            a = int(input(n))
        except (ValueError, TypeError):
            print('\033[0;30;41mErro! Digite Um Número Inteiro Válido!\033[m')
        except (KeyboardInterrupt):
            print('\033[0;30;41mErro! O Usuário Não Digitou Nada.\033[m')
        else:
            return a


def arqexiste(arq):
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
        print('Houve um erro ao tentar criar o arquivo')
    else:
        print(f'Arquivo {arq} Criado!')


def lerarq(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao tentar ler o arquivo')
    else:
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
        print('Ocorreu um erro ao tentar adicionar informações ao arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Os dados não foram adicionados.')
        else:
            print(f'Os Dados de Nome e Idade De {nome} Foram Salvos Na Lista!')

