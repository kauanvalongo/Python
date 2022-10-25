import logging
from re import T
import stdiomask
from os import system
from time import sleep
from getpass import getpass

def leiaint(num):
    while True:
        try:
            n = int(input(num))
        except(TypeError, ValueError, KeyboardInterrupt):
            print('\033[0;30;41mErro! Digite Um Número Válido!\033[m')
        else:
            return n


def menu(n):
    print('-'*42)
    print(f'{"Bem Vindo Ao Sistema De Login Do Kauan..".center(42)}')
    print('-'*42)
    print('[1] - Cadastrar Novo Usuário')
    print('[2] - Fazer Login')
    print('[3] - Sair Do Sistema')
    print('-'*42)
    opc = leiaint(n)
    return opc


def fazer_login():
    login = input('Nome: ')
    senha = stdiomask.getpass(prompt='senha: ', mask='*')
    return(login,senha)


def buscar_usuario(login, senha):
    usuarios = []
    try:
        with open('usuarios.txt', 'r+', encoding='Utf-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(",")
                usuarios.append(linha.split())
            for usuario in usuarios:
                name = usuario[0]
                password = usuario[1]
                if login == name and senha == password:
                    return True
    except(FileNotFoundError):
        return False


while True:
    system('cls')
    opcao = menu('Sua Opção: ')

    if opcao == 1:
        login, senha = fazer_login()
        if login == senha:
            print('Sua Senha Deve Ser Diferente do Seu Nome De Usuário.')
            senha = getpass('Senha: ')
        user = buscar_usuario(login, senha)
        if user == True:
            print('\033[31mUsuário Já Existe.\033[m')
            sleep(2)
        else:
            with open('usuarios.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                arquivo.writelines(f'{login} {senha}\n')
                print('Cadastro Aprovado!')
                exit()
    elif opcao == 2:
        login, senha = fazer_login()
        user = buscar_usuario(login, senha)
        if user == True:
            print('Login Realizado Com Sucesso!')
            sleep(1)
            exit()
        else:
            print('Nome De Usuário e/ou Senha Incorretos...')
            sleep(2)
    elif opcao == 3:
        print('-'*42)
        print(f'{"Sistema Finalizado.".center(42)}')
        sleep(2)
        print('-'*42)
        break
    else:
        print('\033[0;30;41mErro! Digite Um Número Do Menu!\033[m')

