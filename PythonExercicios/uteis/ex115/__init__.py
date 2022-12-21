dic = {}
listanome = []
listaid = []
cadastro = {}
lista = []
olista = []
def nomes(nome):
    global listanome, dic, valor
    while True:
        try:
            c1 = str(input(nome)).strip()
            if c1.isnumeric() or c1 == '':
                print('\033[0;30;41mERRO! Os valores digitados não são válidos.\033[m')
            else:
                listanome.append(c1)
                dic['nome'] = listanome.copy()
                break
        except (TypeError, ValueError, KeyboardInterrupt):
            print('\033[0;30;41mERRO! Os valores digitados não são válidos.\033[m')



def leiaint(n):
    while True:
           try:
            a = str(input(n)).strip()
            if a.isnumeric():
                return int(a)
            else:
                print('\033[0;30;41mERRO. DIGITE UM VALOR INTEIRO.\033[m')
           except:
               print('ERRO. DIGITE UM VALOR INTEIRO.')



def idades(id):
    global listaid, dic, valor
    while True:
        try:
            c2 = int(input(id))
            listaid.append(c2)
            dic['idade'] = listaid.copy()
            break
        except (TypeError, ValueError, KeyboardInterrupt):
            print('\033[0;30;41mERRO! Os valores digitados não são válidos.\033[m')


def cadastros(nome, idade):
    global cadastro, lista, olista
    n = str(input(nome))
    i = int(input(idade))
    lista.append(n)
    cadastro['nomes'] = lista.copy()
    olista.append(i)
    cadastro['idades'] = olista.copy()

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaraquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO. HOUVE UM PROBLEMA NA CRIAÇÃO DO ARQUIVO.')
    else:
        print(f'Arquivo {nome} criado com sucesso..')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao tentar ler o arquivo : ')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace("\n", "")
            print(f'{dado[0]:<30}{dado[1]:>3} Anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro. Algo Deu Errado no Cadastro.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Os registros de nome e idade de {nome} foram adicionados!')
            a.close()
