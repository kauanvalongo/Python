
import requests
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
email = ''
senha = ''

token = '5468560434:AAE11S9PQhsDHzBnrEvbT8K-IOUniPSBbY8'
chat_id = '5085081358'


while True:
    
    service = Service('./chromedriver.exe')
    options = Options()
    options.add_argument('--headless')

    driver = uc.Chrome(service=service)

    driver.get('https://www.playpix.com/pt?openGames=110-real&gameNames=Roulette')
    
    email_input = WebDriverWait(driver, 100).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[3]/div/label/input'))
                        )
    driver.find_element(By.XPATH, '//*[@id="root"]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[3]/div/label/input').send_keys(email)
    sleep(.4)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[4]/div/label/input').send_keys(senha)

    driver.find_element(By.XPATH, '//*[@id="root"]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[6]/div/button').click()
    sleep(10)
    driver.switch_to.frame(0)
    sleep(2)
    driver.switch_to.frame('gameFrame')
    sleep(.5)
    elemento = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[3]/div[11]/div/a')

    link = elemento.get_attribute('href')
    link_token = link

    driver.get(f"{link_token}")

    n = 0
    sleep(4)
    while True:
        try:
            continuar = WebDriverWait(driver, 2).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/button[2]'))
                        )
            
            driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/button[2]').click()
            print('clicou no trço1')
            
        except: pass

        lista_num = []
        lista_num.clear()
        try:
            num1 = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[9]/div[1]/div/span[1]'))
                        )
            
            num2 = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[9]/div[1]/div/span[2]'))
                        )
            
            num3 = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[9]/div[1]/div/span[3]'))
                        )
            
            num4 = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[9]/div[1]/div/span[4]'))
                        )
            
            num5 = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[9]/div[1]/div/span[5]'))
                        )
            
            num6 = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[9]/div[1]/div/span[6]'))
                        )
        
            num7 = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[9]/div[1]/div/span[7]'))
                        )
            
            num8 = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[9]/div[1]/div/span[8]'))
                        )
            
            num9 = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[9]/div[1]/div/span[9]'))
                        )
        
            num10 = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[9]/div[1]/div/span[10]'))
                        )
        



            lista_num.append(num1.text)
            lista_num.append(num2.text)
            lista_num.append(num3.text)
            lista_num.append(num4.text)
            lista_num.append(num5.text)
            lista_num.append(num6.text)
            lista_num.append(num7.text)
            lista_num.append(num8.text)
            lista_num.append(num9.text)
            lista_num.append(num10.text)
            print(lista_num)
        
            n += 1
            if n == 100:
                driver.back()
                sleep(1)
                driver.forward()
                n = 0
                
        except:    

            texto = f'''

            conexão perdida

            '''
            a = texto
            if texto == a:
                        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={texto}'
                        result = requests.get(url_base)
                        driver.close()
                        break
                            
 

# driver.find_element(By.XPATH, '//*[@id="root"]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[3]/div/label/input').send_keys(email)
# sleep(.2)
# driver.find_element(By.XPATH, '//*[@id="root"]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[4]/div/label/input').send_keys(senha)
# sleep(.2)
# driver.find_element(By.XPATH, '//*[@id="root"]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[6]/div/button').click()

# sleep(5)


# driver.execute_script("window.open('https://games.playpix.com/LaunchGame', 'new_window')")

# driver.switch_to.window(driver.window_handles[1])

# sleep(100000)
# driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[2]/ul/li[3]/button').click()
# sleep(10000)

# driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[3]/div[11]/div/a').click()


# sleep(10000)



# sleep(1000)

# //*[@id="app"]/div/div
