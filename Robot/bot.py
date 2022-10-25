import requests
from bs4 import BeautifulSoup
import datetime
from time import sleep
import telebot
import telepot



token = '5468560434:AAE11S9PQhsDHzBnrEvbT8K-IOUniPSBbY8'
chat_id = '5085081358'
texto_atual = ''
jogadas = 0
win = 0
loss = 0
while True:

    documento = requests.get('https://kitblaze.com/double/?visitante=home')
    html_doc = BeautifulSoup(documento.text, 'html.parser')
    ultimos_giros = html_doc.findAll('div', {'class':'giro-img'})
    dic_cores = {'0':'B','1':'V','2':'V','3':'V','4':'V','5':'V','6':'V','7':'V','8':'P','9':'P','10':'P','11':'P','12':'P','13':'P','14':'P'}
    lista = []

    def ultimos():
        for giro in ultimos_giros[100:90:-1]:
            numero = giro.find('span')
            if numero:
                cor = dic_cores[numero.text]
                lista.append(cor)
                print(cor)
         

    def apostas(num): 
        global texto_atual , loss , win , jogadas  
        
        ultimos()

        if num[0:5] == ['P', 'V', 'V', 'V','P'] or num[0:5] == ['P', 'V', 'V', 'V','B']:
            texto = '''✅GREEN No ⚫'''
            if texto != texto_atual:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto
                jogadas += 1
                win += 1
                sleep(5)
            else:
                sleep(5)
                pass

        elif num[0:4] == ['V', 'V', 'V', 'V'] or num[0:4] == ['B', 'V', 'V', 'V']:          
            texto = '''🔴 LOSS '''
            if texto != texto_atual:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto
                jogadas += 1
                loss += 1
                sleep(5)
            else:
                sleep(5)
                pass

        elif num[0:3] == ['V', 'V', 'V']:        
            texto = '''
            ✅Entrada Confirmada! Entrar No ⚫
            Buscar Apoio No ⚪'''
            if texto != texto_atual:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto
                sleep(5)
            else:
                sleep(5)
                pass

        elif num[0:2] == ['V', 'V']:           
            texto = '''
                Atenção!!!
            ✅Possível Entrada No ⚫ 
            Buscar Apoio No ⚪'''
            if texto != texto_atual:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto
                sleep(5)
            else:
                sleep(5)
                pass

        elif num[0:4] == ['P','P', 'P', 'P'] or num[0:4] == ['B', 'P', 'P', 'P']:         
            texto = '''🔴 LOSS '''
            if texto != texto_atual:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto
                jogadas += 1
                loss += 1
                sleep(5)
            else:
                sleep(5)
                pass

        elif num[0:5] == ['V', 'P', 'P', 'P','V'] or num[0:5] == ['V', 'P', 'P', 'P','B']:        
            texto = '''✅GREEN No 🔴'''
            if texto != texto_atual:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto
                jogadas += 1
                win += 1
                sleep(5) 
            else:
                sleep(5)
                pass


        elif num[0:3] == ['P', 'P', 'P']:         
            texto = '''
            ✅Entrada Confirmada, Entrar No 🔴
            Buscar Apoio No ⚪'''
            if texto != texto_atual:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto
                sleep(5)
            else:
                sleep(5)
                pass

        elif num[0:2] == ['P', 'P']:          
            texto = '''
                Atenção!!
            ✅Possível Entrada No 🔴 
            Buscar Apoio No ⚪
            '''
            if texto != texto_atual:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto
                sleep(5)
            else:
                sleep(5)
                pass
            
        elif num[0:5] == ['P', 'P','V','P','P']:          
            texto = '''
                Atenção!
            ✅Possível Entrada No 🔴 
            Buscar Apoio No ⚪
            '''
            if texto != texto_atual:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto
                sleep(5)
            else:
                sleep(5)
                pass

        elif num[0:5] == ['V', 'V','P','V','V']:          
            texto = '''
                Atenção!
            ✅Possível Entrada No ⚫ 
            Buscar Apoio No ⚪
            '''
            if texto != texto_atual:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto
                sleep(5)
            else:
                sleep(5)
                pass
    

    print(f'o número de Resultados é : {jogadas}, {win} Foram Lucro, {loss} Foram Perda')            


    apostas(lista)
    sleep(5)
