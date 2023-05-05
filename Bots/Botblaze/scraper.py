from re import I, T
import requests
from bs4 import BeautifulSoup
import datetime
from time import sleep
import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from undetected_chromedriver import ChromeOptions, Chrome



token = '5468560434:AAE11S9PQhsDHzBnrEvbT8K-IOUniPSBbY8'
chat_id = '5085081358'
texto_atual = ''
texto_atual2 = ''
total_v = 0
total_p = 0
total_b = 0

def pegar_dados():

    while True:
        
        documento = requests.get('https://kitblaze.com/double/?visitante=home')
        html_doc = BeautifulSoup(documento.text, 'html.parser')
        ultimos_giros = html_doc.findAll('div', {'class':'giro-img'})
        dic_cores = {'0':'B','1':'V','2':'V','3':'V','4':'V','5':'V','6':'V','7':'V','8':'P','9':'P','10':'P','11':'P','12':'P','13':'P','14':'P'}
        lista = []

        def ultimos():
            for giro in ultimos_giros[40:100:1]:
                numero = giro.find('span')
                if numero:
                    cor = dic_cores[numero.text]

                    lista.append(cor) 
                    

                    
        ultimos()
        return lista
pegar_dados()
        
def total():
    while True:
        total_v = 0
        total_p = 0
        total_b = 0
        documento = requests.get('https://kitblaze.com/double/?visitante=home')
        html_doc = BeautifulSoup(documento.text, 'html.parser')
        ultimos_giros = html_doc.findAll('div', {'class':'giro-img'})
        dic_cores = {'0':'B','1':'V','2':'V','3':'V','4':'V','5':'V','6':'V','7':'V','8':'P','9':'P','10':'P','11':'P','12':'P','13':'P','14':'P'}
        lista = []
        lista_total = []

        def ultimos():
            for giro in ultimos_giros[40:100:1]:
                numero = giro.find('span')
                if numero:
                    cor = dic_cores[numero.text]

                    lista.append(cor)                  
        ultimos()


        for letra in lista:
            if letra == "V":
                total_v += 1
            elif letra == "P":
                total_p += 1
            elif letra == "B":
                total_b += 1  

        lista_total.append(total_v)
        lista_total.append(total_p)
        lista_total.append(total_b)

        print(lista_total)

        return lista_total      
    
total()



def perdas_blaze():
    lista_num = []
    lista_num2 = []
    valores_inteiros = []
    link_token = 'https://blaze.com/pt/games/double'
    service = Service('./chromedriver.exe')
    # options.add_argument("--disable-gpu")
    while True:    
        
        options = ChromeOptions()

    
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument('--headless')
        

        driver = uc.Chrome( service=service, options=options)
        print('driver doido')
        driver.get(f"{link_token}")

        sleep(2)
        valorv = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/span'))
                    )
        valorv = valorv.text
        valorv = valorv.replace('R$', '').replace(' ', '')

        valorp = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[3]/div/div[3]/div[1]/div[2]/span'))
                    )
        valorp = valorp.text
        valorp = valorp.replace('R$', '').replace(' ', '')

        valorb = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[2]/div/div[3]/div[1]/div[2]/span'))
                    )
        valorb = valorb.text
        valorb = valorb.replace('R$', '').replace(' ', '')

        lista_num.append(valorv)
        lista_num.append(valorp)
        lista_num.append(valorb)

        sleep(2)
        valorv2 = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/span'))
                    )
        valorv2 = valorv2.text
        valorv2 = valorv2.replace('R$', '').replace(' ', '')
        


        valorp2 = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[3]/div/div[3]/div[1]/div[2]/span'))
                    )
        valorp2 = valorp2.text
        valorp2 = valorp2.replace('R$', '').replace(' ', '')

        valorb2 = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[2]/div/div[3]/div[1]/div[2]/span'))
                    )
        valorb2 = valorb2.text
        valorb2 = valorb2.replace('R$', '').replace(' ', '')

        lista_num.append(valorv2)
        lista_num.append(valorp2)
        lista_num.append(valorb2)
        print(lista_num)
        
        if lista_num[0] == lista_num[3] and lista_num[1] ==lista_num[4] and lista_num[2] == lista_num[5]:
            
            print('Rodada finalizada')
            sleep(12)
            branco = False
            try:
                branco = WebDriverWait(driver, 1).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="roulette-recent"]/div/div[1]/div[1]/div/div/img'))
                        )
                branco = True
            except: pass
            if not branco:
                ultimo_giro = WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="roulette-recent"]/div/div[1]/div[1]/div/div/div'))
                        )
                print(ultimo_giro.text)

                if ultimo_giro.text == '1' or ultimo_giro.text == '2' or ultimo_giro.text == '3' or ultimo_giro.text == '4' or ultimo_giro.text == '5' or ultimo_giro.text == '6' or ultimo_giro.text == '7':
                    ultimo_giro = 'V'
                    print(ultimo_giro)

                elif ultimo_giro.text == '8' or ultimo_giro.text == '9' or ultimo_giro.text == '10' or ultimo_giro.text == '11' or ultimo_giro.text == '12' or ultimo_giro.text == '13' or ultimo_giro.text == '14':
                    ultimo_giro = 'P'
                    print(ultimo_giro)
            else:
                giro_branco = 'B'
                print(giro_branco)
                driver.quit()

            # return(lista_num)
            
        # valores_inteiros.clear()
            driver.quit()
            return lista_num
        
            
        driver.quit()
        lista_num.clear()
        # valores_inteiros.clear()
        
        sleep(2)


perdas_blaze()

    







def gerar_numero_aleatorio():
    while True:
        total_v = 0
        total_p = 0
        total_b = 0

        percent_v = ''
        percent_p = ''
        percent_b = ''

        documento = requests.get('https://kitblaze.com/double/?visitante=home')
        html_doc = BeautifulSoup(documento.text, 'html.parser')
        ultimos_giros = html_doc.findAll('div', {'class':'giro-img'})
        dic_cores = {'0':'B','1':'V','2':'V','3':'V','4':'V','5':'V','6':'V','7':'V','8':'P','9':'P','10':'P','11':'P','12':'P','13':'P','14':'P'}
        lista = []
        lista_total = []
        lista_numeros = []

        def ultimos():
            for giro in ultimos_giros[40:100:1]:
                numero = giro.find('span')
                if numero:
                    cor = dic_cores[numero.text]

                    lista.append(cor)    
        ultimos()

        for letra in lista:
            if letra == "V":
                total_v += 1
            elif letra == "P":
                total_p += 1
            elif letra == "B":
                total_b += 1  

        lista_total.append(total_v)
        lista_total.append(total_p)
        lista_total.append(total_b)     

        if lista[59] == 'V': 
            # opcoes = 1
            # if opcoes == 1:
            percent_v = '59,5%'
            percent_p = '36,6'
            percent_b = '3,9'  
            lista_numeros.append(percent_v) 
            lista_numeros.append(percent_p)  
            lista_numeros.append(percent_b) 
            # print(lista[59])


        elif lista[59] == 'P': 
            # opcoes = 1
            # if opcoes == 1:
            percent_p = '59,5%'
            percent_v = '36,6'
            percent_b = '3,9'  
            lista_numeros.append(percent_v) 
            lista_numeros.append(percent_p)  
            lista_numeros.append(percent_b)   

        
            print(lista[59])
        print(lista_numeros)
        return lista_numeros


gerar_numero_aleatorio()