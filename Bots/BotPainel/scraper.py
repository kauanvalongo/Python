from re import I, T
import requests
from bs4 import BeautifulSoup
from time import sleep

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from undetected_chromedriver import ChromeOptions, Chrome
# from undetected_chromedriver import ChromeDriverManager



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
    




def perdas_blaze():
    sleep(10)
    lista_num = []
    link_token = 'https://blaze.com/pt/games/double'
    service = Service('./chromedriver.exe')
    service.command_line_args()[:] = [
            '--disable-extensions',  # Desativar extensões do Chrome
            '--disable-gpu',  # Desativar aceleração de GPU     
        ]
    options = ChromeOptions()
    options.add_argument(f"--window-size={1920},1080")
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service,options=options)
    driver.get(f"{link_token}")
    while True:
        sleep(.5)
        valorv = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/span'))
                    )
        valorv = valorv.text
        if valorv == '':
            sleep(2)
            valorv = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/span'))
                    )
            valorv = valorv.text
            if valorv == '':
                sleep(2)
                valorv = WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/span'))
                        )
                valorv = valorv.text
                if valorv == '':
                    driver.close()               
        valorv = valorv.replace('R$', '').replace(' ', '')
        valorvreal = valorv.replace('.', '').replace(',', '.')
        valorvreal = float(valorvreal)
        valorvreal = round(valorvreal, 2)
        valorp = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[3]/div/div[3]/div[1]/div[2]/span'))
                    )
        valorp = valorp.text
        valorp = valorp.replace('R$', '').replace(' ', '')
        valorpreal = valorp.replace('.', '').replace(',', '.')
        valorpreal = float(valorpreal)
        valorpreal = round(valorpreal, 2)
        valorb = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[2]/div/div[3]/div[1]/div[2]/span'))
                    )
        valorb = valorb.text
        valorb = valorb.replace('R$', '').replace(' ', '')
        valorbreal = valorb.replace('.', '').replace(',', '.')
        valorbreal = float(valorbreal)
        valorbreal = round(valorbreal, 2)
        lista_num.append(valorv)
        lista_num.append(valorp)
        lista_num.append(valorb)
        sleep(.5)
        valorv2 = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/span'))
                    )
        valorv2 = valorv2.text
        if valorv2 == '':
            sleep(2)
            valorv2 = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/span'))
                    )
            valorv2 = valorv2.text
        if valorv2 == '':
            sleep(2)
            valorv2 = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/span'))
                    )
            valorv2 = valorv2.text
        valorv2 = valorv2.replace('R$', '').replace(' ', '')
        valorv2real = valorv2.replace('.', '').replace(',', '.')
        valorv2real = float(valorv2real)
        
        valorp2 = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[3]/div/div[3]/div[1]/div[2]/span'))
                    )
        valorp2 = valorp2.text
        valorp2 = valorp2.replace('R$', '').replace(' ', '')
        valorp2real = valorp2.replace('.', '').replace(',', '.')
        valorp2real = float(valorp2real)
        valorb2 = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="roulette"]/div/div[2]/div/div[2]/div/div[3]/div[1]/div[2]/span'))
                    )
        valorb2 = valorb2.text
        valorb2 = valorb2.replace('R$', '').replace(' ', '')
        valorb2real = valorb2.replace('.', '').replace(',', '.')
        valorb2real = float(valorb2real)
        lista_num.append(valorv2)
        lista_num.append(valorp2)
        lista_num.append(valorb2)
        print(lista_num) 
        if lista_num[0] == lista_num[3] and lista_num[1] ==lista_num[4] and lista_num[2] == lista_num[5]:   
            print('Rodada finalizada')
            lista_num.append(valorvreal)
            lista_num.append(valorpreal)
            lista_num.append(valorbreal)   
            driver.close()
            print(lista_num)
            return lista_num          
        else:
            lista_num.clear()
            pass
            
     
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


