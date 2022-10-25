from asyncore import read
from fileinput import close
from optparse import Values
from timeit import repeat
from tkinter import Button
import PySimpleGUI as sg
import os
from time import sleep


sg.theme('BlueMono')
layout = [
        [sg.Text('Usuário', font=12, size=(10, 1)),
        sg.Input(key='login', font=12, size=(20, 1))],
        [sg.Text('Senha', font=12, size=(10, 1)),
        sg.Input(key='senha', password_char='*', font=12, size=(20, 1))],
        [sg.Button('Novo Usuário', font=12),sg.Button('Fazer Login', font=12),sg.Button('Sair', font=12)]
        ]        


janela = sg.Window('Login', layout, font=14) 
evento, valores = janela.Read()
val = valores['login']
sen = valores['senha']


def sai(): 
    sair = [
    [sg.Text('Programa Finalizado..')],
    [sg.Button('Fechar')]
    ]
    janela_sai = sg.Window('Finalizando..', sair, font=14)
    evento, valores = janela_sai.Read()
    if evento == 'Fechar' or evento == sg.WIN_CLOSED:
        janela_sai.close()


def nao_existe():
    nexis = [
        [sg.Text('Erro! O Usuário Não Existe.')],
        [sg.Button('Voltar')],
    ]
    janela_nexis = sg.Window('Erro!', nexis, font=14)
    evento, valores = janela_nexis.Read()
    if evento == 'Voltar' or evento == sg.WIN_CLOSED:
        janela_nexis.close()


def dados_jaexiste():
    jaexiste = [
        [sg.Text('Erro! O Usuário Já Está Cadastrado!')],
        [sg.Button('Voltar')],
    ]
    janela_jaexiste = sg.Window('Erro!', jaexiste, font=14)
    evento, valores = janela_jaexiste.Read()
    if evento == 'Voltar' or evento == sg.WIN_CLOSED:
        janela_jaexiste.close()


def dados_inv():
    inv = [
        [sg.Text('Dados Inválidos! Preencha os Campos Corretamente!')],
        [sg.Button('Voltar')],
    ]
    janela_inv = sg.Window('Erro!', inv, font=14)
    evento, valores = janela_inv.Read()
    if evento == 'Voltar' or evento == sg.WIN_CLOSED:
        janela_inv.close()


def novo_cadastro():
    janela.hide()
    novo = [
        [sg.Text('Cadastro Efetuado Com Sucesso!')],
        [sg.Button('Voltar')],
    ]
    janela_novo = sg.Window('Aprovado!', novo, font=14)
    evento, valores = janela_novo.Read()
    if evento == 'Voltar' or evento == sg.WIN_CLOSED:
        janela_novo.close()
    janela['login'].update('')
    janela['senha'].update('')
    janela.un_hide()


def login_efetuado():
    janela['login'].update('')
    janela['senha'].update('')
    janela.hide()
    login = [
        [sg.Text(f'Bem Vindo {val}, Login Efetuado Com Sucesso!')],
        [sg.Button('Logout')],
    ]
    janela_login = sg.Window('Conectado!', login, font=14)
    evento, valores = janela_login.Read()
    if evento == 'Logout' or evento == sg.WIN_CLOSED:
        janela_login.close()
    janela.un_hide()

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
    evento, valores = janela.Read()
    val = valores['login']
    sen = valores['senha']
    if evento == sg.WIN_CLOSED or evento == 'Sair':
        janela.close()
        sai() 
        break
    elif evento == 'Fazer Login':  
        if buscar_usuario(valores['login'], valores['senha']) == True:
            login_efetuado()
        else:
            nao_existe()               
    elif evento == 'Novo Usuário':
        if buscar_usuario(valores['login'], valores['senha']) == True:  
            dados_jaexiste()

        elif valores['login'] != '' and valores['senha'] != '':
            with open('usuarios.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                    arquivo.writelines(f'{val} {sen}\n')
                    novo_cadastro() 
        else:
            dados_inv()               


janela.close()
