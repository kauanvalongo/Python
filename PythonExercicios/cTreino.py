from uteis.treino2 import *
from time import sleep

arq = 'Akauannn.txt'

if not arqexiste(arq):
    criarq(arq)

while True:
    resposta = menu(['Ver Cadastros', 'Cadastrar Nova Pessoa', 'Sair do Programa'])
    if resposta == 3:
        cabeca('SISTEMA FINALIZADO...')
        sleep(1)
        break
    elif resposta == 2:
        cabeca('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        addarq(arq, nome, idade)
        sleep(2)
    elif resposta == 1:
        cabeca('PESSOAS CADASTRADAS')
        lerarq(arq)
        sleep(2)
    else:
        print('\033[0;30;41mErro! Digite Um Valor Do Menu.\033[m')
        sleep(2)
