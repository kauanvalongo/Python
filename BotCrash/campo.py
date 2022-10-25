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
while True:

    documento = requests.get('https://kitblaze.com/crash/?visitante=home')
    html_doc = BeautifulSoup(documento.text, 'html.parser')
    bons_giros = html_doc.findAll('div', {'class':'bom'})
    ruins_giros = html_doc.findAll('div', {'class':'ruim'})
    dic_num = {}
    listabom = []
    listaruim = []
    listatot = []
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
            


            
    def marcabom():
        global listabom, ultimo_num_bom
        bons()
        n1 = listabom[0]
        n2 = listabom[1]
        n3 = listabom[2]
        n4 = listabom[3]
        n5 = listabom[4]
        n6 = listabom[5]
        n7 = listabom[6]
        n8 = listabom[7]
        n9 = listabom[8]
        n10 = listabom[9]
        num = n1
        if num != ultimo_num_bom:
            ultimo_num_bom = num
            print(ultimo_num_bom)
            return ultimo_num_bom
        else:
            return False

         
    def marcaruim():
        global listaruim, ultimo_num_ruim
        ruins()
        r1 = listaruim[0]
        r2 = listaruim[1]
        r3 = listaruim[2]
        r4 = listaruim[3]
        r5 = listaruim[4]
        r6 = listaruim[5]
        r7 = listaruim[6]
        r8 = listaruim[7]
        r9 = listaruim[8]
        r10 = listaruim[9]
        num = r1
        if num != ultimo_num_ruim:
            ultimo_num_ruim = num
            print(ultimo_num_ruim)
            return ultimo_num_ruim
        else:
            return False
            

    def apostas(): 
        global texto_atual , loss , win , jogadas  
        
        inc = marcabom()
        

        if inc == 'X':
            texto = f'''
            Último GALE
            Entrada Confirmada✅
            Sair No 4x'''
            if texto != texto_atual:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto          
            else:
                pass
    
    def lista():     
        bom = marcabom()      
        listatot.append(bom)
        ruim = marcaruim()
        listatot.append(ruim)   
        print(listatot)
        sleep(3)
    

    lista()

