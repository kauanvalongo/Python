from re import I, T
import requests
from bs4 import BeautifulSoup
import datetime
from time import sleep
import telebot
import telepot


token = '5468560434:AAE11S9PQhsDHzBnrEvbT8K-IOUniPSBbY8'
chat_id = '5085081358'
texto_atual = ''
texto_atual2 = ''
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
        global texto_atual , loss , win , jogadas , vezes, comeca, chat_id, token, inc, gale , texto_atual2
        try:
            inc = float(marcador())         
            if inc < 1.1 :
                comeca = True
                vezes = 0
                texto = f'''
<<< CRASH >>>
GALE Avistado: {inc}X
Entrada Confirmada após 5 Crashes✅
                '''
                if texto != texto_atual and texto != texto_atual2:
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
<<< CRASH >>>
Entrada Confirmada!✅
Sair No 2X🔴
            '''
            if texto != texto_atual and texto != texto_atual2:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto          
            else:
                pass
        
        elif vezes == 6 and gale < 2 :
            texto ='''
            LOSS🔴
            '''
            if texto != texto_atual and texto != texto_atual2:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto   
                loss += 1 
                jogadas += 1      
            else:
                pass
                           

        elif vezes == 6 and gale >= 2 :
            texto ='''
            WIN✅
            '''
            if texto != texto_atual and texto != texto_atual2:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual = texto 
                win += 1
                jogadas += 1        
            else:
                pass
                
        else:
            pass
        

    
    documento2 = requests.get('https://kitblaze.com/double/?visitante=home')
    html_doc2 = BeautifulSoup(documento2.text, 'html.parser')
    ultimos_giros2 = html_doc2.findAll('div', {'class':'giro-img'})
    dic_cores2 = {'0':'B','1':'V','2':'V','3':'V','4':'V','5':'V','6':'V','7':'V','8':'P','9':'P','10':'P','11':'P','12':'P','13':'P','14':'P'}
    lista2 = []

    def ultimos2():
        for giro in ultimos_giros2[100:90:-1]:
            numero = giro.find('span')
            if numero:
                cor = dic_cores2[numero.text]
                lista2.append(cor)
                print(cor)
         

    def apostas2(num): 
        global texto_atual , loss , win , jogadas  , texto_atual2
        
        ultimos2()

        if num[0:5] == ['P', 'V', 'V', 'V','P'] or num[0:5] == ['P', 'V', 'V', 'V','B']:
            texto = '''✅GREEN No ⚫'''
            if texto != texto_atual and texto != texto_atual2:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual2 = texto
                jogadas += 1
                win += 1

            else:
                
                pass

        elif num[0:4] == ['V', 'V', 'V', 'V'] or num[0:4] == ['B', 'V', 'V', 'V']:          
            texto = '''🔴 LOSS '''
            if texto != texto_atual and texto != texto_atual2:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual2 = texto
                jogadas += 1
                loss += 1

            else:
                
                pass

        elif num[0:3] == ['V', 'V', 'V']:        
            texto = '''
<<< DOUBLE >>>            
✅Entrada Confirmada! Entrar No ⚫
Buscar Apoio No ⚪'''
            if texto != texto_atual and texto != texto_atual2:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual2 = texto

            else:
                
                pass

        elif num[0:2] == ['V', 'V']:           
            texto = '''
<<< DOUBLE >>>           
Atenção!!!
✅Possível Entrada No ⚫ 
Buscar Apoio No ⚪'''
            if texto != texto_atual and texto != texto_atual2:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual2 = texto

            else:
                
                pass

        elif num[0:4] == ['P','P', 'P', 'P'] or num[0:4] == ['B', 'P', 'P', 'P']:         
            texto = '''🔴 LOSS '''
            if texto != texto_atual and texto != texto_atual2:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual2 = texto
                jogadas += 1
                loss += 1

            else:
                
                pass

        elif num[0:5] == ['V', 'P', 'P', 'P','V'] or num[0:5] == ['V', 'P', 'P', 'P','B']:        
            texto = '''✅GREEN No 🔴'''
            if texto != texto_atual and texto != texto_atual2:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual2 = texto
                jogadas += 1
                win += 1

            else:
                
                pass


        elif num[0:3] == ['P', 'P', 'P']:         
            texto = '''
<<< DOUBLE >>>
✅Entrada Confirmada, Entrar No 🔴
Buscar Apoio No ⚪'''
            if texto != texto_atual and texto != texto_atual2:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual2 = texto

            else:
                
                pass

        elif num[0:2] == ['P', 'P']:          
            texto = '''
<<< DOUBLE >>>
Atenção!!
✅Possível Entrada No 🔴 
Buscar Apoio No ⚪
            '''
            if texto != texto_atual and texto != texto_atual2:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual2 = texto

            else:
                
                pass
            
        elif num[0:5] == ['P', 'P','V','P','P']:          
            texto = '''
<<< DOUBLE >>>
Atenção!
✅Possível Entrada No 🔴 
Buscar Apoio No ⚪
            '''
            if texto != texto_atual and texto != texto_atual2:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual2 = texto

            else:
                
                pass

        elif num[0:5] == ['V', 'V','P','V','V']:          
            texto = '''
<<< DOUBLE >>>           
Atenção!
✅Possível Entrada No ⚫ 
Buscar Apoio No ⚪
            '''
            if texto != texto_atual and texto != texto_atual2:
                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                result = requests.get(url_base)
                texto_atual2 = texto
                
            else:
                
                pass
    

    print(f'o número de Resultados é : {jogadas}, {win} Foram Lucro, {loss} Foram Perda')            


    apostas2(lista2)
            

    
    apostas()
      
    
      
    
