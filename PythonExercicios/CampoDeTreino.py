from uteis.Treino import *
from time import sleep
arq = 'abcd.txt'

if not arquivoexiste(arq):
    criarq(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Dasastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 3:
        cabecalho('PROGRAMA FINALIZADO...')
        break
    elif resposta == 2:
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        addarq(arq, nome, idade)
    elif resposta == 1:
        lerarq(arq)
    else:
        print('\033[0;30;41mERRO! Digite um número válido\033[m')
    sleep(2)
