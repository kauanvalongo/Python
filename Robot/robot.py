import telebot
import requests
from bs4 import BeautifulSoup


token = '5468560434:AAE11S9PQhsDHzBnrEvbT8K-IOUniPSBbY8'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["versinais"])
def versinais(msg):
    sinais = f"""
Sinal Mais Recente:

    

Boa Sorte!

O Que Deseja?
/versinais Para Ver O Sinal Mais Recente
/jogar Para Fazer Uma Aposta Automática
/parar Para Desligar o Bot"""
    bot.reply_to(msg, sinais)    

@bot.message_handler(commands=["jogar"])
def jogar(msg):
    jogar = """
O Bot Fez Uma Jogada Pra Você!
...
...
...
Win! 
Você Ganhou R$246,34 na Plataforma!

O Que Deseja?
/versinais Para Ver O Sinal Mais Recente
/jogar Para Fazer Uma Aposta Automática
/parar Para Desligar o Bot"""
    bot.reply_to(msg, jogar)

@bot.message_handler(commands=["parar"])
def parar(msg):
    parar = """
Bot Desligando..."""
    bot.reply_to(msg, parar)


def verificar(msg):
    return True

@bot.message_handler(func=verificar)
def responder(msg):
    texto = """
Olá, Seja Bem Vindo!
O Que Deseja?
/versinais Para Ver O Sinal Mais Recente
/jogar Para Fazer Uma Aposta Automática
/parar Para Desligar o Bot
Boa Sorte!"""
    bot.reply_to(msg, texto)

bot.polling()