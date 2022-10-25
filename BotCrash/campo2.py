from re import I
import requests
from bs4 import BeautifulSoup
import datetime
from time import sleep
import telebot
import telepot


token = '5468560434:AAE11S9PQhsDHzBnrEvbT8K-IOUniPSBbY8'
chat_id = '5085081358'
texto_atual = ''
novos_atual = ''
jogadas = 0
win = 0
loss = 0
ultimo_num_bom = ''
ultimo_num_ruim = ''
num = ''
ultimo_num = ''
vezes = 0
comeca = False
ene1 = 0
ere1 = 0
gale = ''
numero = ''
while True:

    documento = requests.get('https://kitblaze.com/crash/?visitante=home')
    html_doc = BeautifulSoup(documento.text, 'html.parser')
    bons_giros = html_doc.findAll('div', {'class':'bom'})
    ruins_giros = html_doc.findAll('div', {'class':'ruim'})
    dic_num = {}
    listabom = []
    listaruim = []
    listatot = []
    novalista = []
    id = []
    
    def bons():
        for giro in bons_giros :
            numero = giro.text
            a = numero.replace('X', '')
            f = float(a)
            if f :
                listabom.append(f)
           
 

    def ruins():
        for giro in ruins_giros :
            numero = giro.text
            a = numero.replace('X', '')
            f = float(a)
            if f:
                listaruim.append(f)
            


            
    def marcador():
        global listabom, ultimo_num_bom, listaruim, ultimo_num_ruim, num, ultimo_num, novalista, ene1, ere1
        media = 2
        bons()
        n1 = listabom[0]
    
        ruins()
        r1 = listaruim[0]
        
        if n1 >= 2 and n1 != ultimo_num_bom:
            num = n1         
            ultimo_num_bom = n1
            listatot.append(ultimo_num_bom)
            print(ultimo_num_bom)
            return ultimo_num_bom
        elif r1 < 2 and r1 != ultimo_num_ruim:
            num = r1
            ultimo_num_ruim = r1           
            listatot.append(ultimo_num_ruim)
            print(ultimo_num_ruim)
            return ultimo_num_ruim
        else:
            pass


    def apostas(): 
        global texto_atual , loss , win , jogadas , vezes, comeca, chat_id, token, inc, gale 
        try:
            inc = float(marcador())         
            if inc < 1.1 :
                comeca = True
                vezes = 0
                texto = f'''
GALE Avistado: {inc}X
Entrada Confirmada após 5 Crashes✅
                '''
                if texto != texto_atual:
                    url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                    result = requests.get(url_base)
                    texto_atual = texto          
                else:
                    pass

            elif inc >= 1.1 and comeca == True:
                if gale != inc:
                    vezes += 1
                    gale = inc 
                       
        except:
            pass


        if vezes == 5: 
            texto = f''' 
Entrada Confirmada!✅
Sair No 2X🔴
            '''
            if texto != texto_atual:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto          
            else:
                pass
        
        elif vezes == 6 and gale < 2 :
            texto ='''
            LOSS🔴
            '''
            if texto != texto_atual:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto          
            else:
                pass
                           

        elif vezes == 6 and gale >= 2 :
            texto ='''
            WIN✅
            '''
            if texto != texto_atual:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto          
            else:
                pass
                
        else:
            pass
        
    apostas()
    if numero != vezes:
        print(vezes)
        numero = vezes  
    
      
    
