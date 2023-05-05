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
    link_token = 'https://br.betano.com'

    service = Service('./chromedriver.exe')
    options = Options()

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

    options.add_argument(f"user-agent={headers['User-Agent']}")

    driver = uc.Chrome(service=service, options=options)

    driver.get(f"{link_token}")

    n = 0
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="landing-page-modal"]/div/div[2]/div[1]/p[2]/a').click()
    sleep(10)
    driver.switch_to.frame(1)
    sleep(3)
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(email)
    sleep(.4)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(senha)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/section/div/form/button').click()
    driver.switch_to.default_content()
    sleep(4)
    

    driver.get('https://br.betano.com/casino/live/games/auto-roulette-2/444/tables/107175/')

    sleep(20)

    driver.get('https://cachedownload-br.p-content.gambling-malta.com/live/bundles/23.3.0.20/?game=rol&launch_alias=rol_autoroulette2&lobby=https%3A%2F%2Fbr.betano.com%2Fcasino%2Flobbyredirect&language=PT-BR&clienttype=casino&redirect_time=1678984578751&backUrl=https%3A%2F%2Fcachedownload-br.p-content.gambling-malta.com%2Flive%2F%3Fgame%3Drol%26launch_alias%3Drol_autoroulette2%26lobby%3Dhttps%253A%252F%252Fbr.betano.com%252Fcasino%252Flobbyredirect%26language%3DPT-BR%26clienttype%3Dcasino#/')
    sleep(10)



    while True:
        




        try:
            continuar = WebDriverWait(driver, 2).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[5]/div/div[2]/div/div[3]/button'))
                        )
            
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[5]/div/div[2]/div/div[3]/button').click()
            print('clicou no trço1')
            
        except: pass
        try:
            click = WebDriverWait(driver, 2).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="playButton-playerDiv_e443087f-a2ee-5f0f-71f5-a6367a76387d"]/path'))
                            )
            print('botaoclick')
            driver.back()
            sleep(.4)
            driver.forward()


        except:pass

        lista_num = []
        lista_num.clear()
        try:
            num1 = WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div[8]/div/div[2]/div/div[1]'))
                        )
            
            num2 = WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div[8]/div/div[2]/div/div[2]'))
                        )
            
            num3 = WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div[8]/div/div[2]/div/div[3]'))
                        )
            
            num4 = WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div[8]/div/div[2]/div/div[4]'))
                        )
            
            num5 = WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div[8]/div/div[2]/div/div[5]'))
                        )
            
            num6 = WebDriverWait(driver, 500).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div[8]/div/div[2]/div/div[6]'))
                        )
        
            num7 = WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div[8]/div/div[2]/div/div[7]'))
                        )
            
            num8 = WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div[8]/div/div[2]/div/div[8]'))
                        )
            
            num9 = WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div[8]/div/div[2]/div/div[9]'))
                        )
        
            num10 = WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div[8]/div/div[2]/div/div[10]'))
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
            print(n)
            if n == 35:
                driver.back()
                sleep(1)
                driver.forward()
                n = 0
        except: 
            driver.back()
            sleep(1)
            driver.forward()
                        
        

                       
                            
 

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