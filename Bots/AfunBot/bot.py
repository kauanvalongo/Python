#downloads necessarios para o bot funcionar em seu computador

#Python3 -  'https://www.python.org/downloads/' baixe o python3 na sua última versão, lembre-se de checar se seu windows(ou correspondente) é 64b ou 32b.

#link do vídeo mostrando como fazer o donwload do python3: 'https://www.youtube.com/watch?v=VuKvR1J2LQE&t=944s' minuto 7:55 até 10:25



#VisualStudio - 'https://code.visualstudio.com/download' : programa para ler o código

#link do vídeo mostrando como fazer o donwload do vscode: 'https://www.youtube.com/watch?v=VuKvR1J2LQE&t=944s' minuto 5:00 até 12:00


#driver - 'https://sites.google.com/a/chromium.org/chromedriver/downloads' : robô que vai entrar no site 

#link do vídeo mostrando como fazer o donwload do driver: 'https://www.youtube.com/watch?v=Ot10qzrb13c&t=242s' minuto 0:15 até 2:33, perceba que ele cria uma pasta e deixa ela junto do chrome driver, isso se dá porque para o bot funcionar o driver precisa estar na mesma pasta que o código. você pode fazer igual ele faz no video e colocar 'afunbot.py' como o nome do novo arquivo


#Após todas as instalações, abra o visualstudio, coloque o código dentro de 'afunbot.py' que você acabou de criar

#por ultimo, clique em : 'terminal' em algum lugar acima do código e digite os seguintes comandos;




#  ' pip install requests ' | depois aperte enter e espere

#  ' pip install selenium ' | depois aperte enter e espere

#  ' pip install undetected_chromedriver ' | depois aperte enter e espere


# Com tudo isso feito, o seu bot está pronto para rodar! aperte a setinha no canto superior direito para iniciar o bot, e caso queira parar ou reiniciar ele, aperte um quadrado vermelho que irá aparecer após clicar na seta



import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service



token = '5468560434:AAE11S9PQhsDHzBnrEvbT8K-IOUniPSBbY8'
chat_id = '5085081358'

chat_id_esp = ''

chat_id_ing = ''


texto_atual = ''
texto_atual2 = ''

texto_atual_esp = ''
texto_atual2_esp = ''

texto_atual_ing = ''
texto_atual2_ing = ''


wins = 0
loss = 0


#O bot vai copiar e colar essas credencias para fazer login no site

#Estes campos devem ser preenchidos.
user = ''
senha=''


lista_cores = []



# Abaixo, o controle de espera para o bot fazer as coisas, caso seu pc seja fraco, tente aumentar alguns desses parametros, o '.4' significa 0,4 segundos. 

#Tempo para abrir o site, fazer login e entrar no jogo.
tempo1 = .4

#Tempo para abrir o segundo site.
tempo2 = 3



# Abaixo, os textos que serão enviados para cada canal, você pode modificar ele para colocar um emoji mais bonito ou melhorar o texto quando quiser. lembre-se de ter cuidado para não mexer no link, você só pode modificar o emoji atras da primeira seta '<'

#Lembre-se de que sempre que algo for modificado no código, você precisa ligar e desligar o robô para atualizar as novas informações.



#aqui você pode modificar o link e a mensagem de convite, lembrando que ambos devem estar entre aspas sempre.
link_convite = 'https://www.afun.com/game/101803096/Football-Studio'
mensagem_convite = 'Entre Na Sala'


texto_entrada_vermelho_pt =f'''

⬛ENTRADA CONFIRMADA⬛
♠️Cards:FootBall Studio
🃏Apostar na Cor:🔴
🚨Cubra o Empate

👉<a href='{link_convite}'>{mensagem_convite}</a>
    
'''


texto_win_vermelho_pt = '''

GREEN! RECEBA! 🔴

'''

texto_martingale_vermelho_pt = '''

🚨O ideal é Fazer um Maximo de 2 Gales: 🔴

'''


texto_loss_vermelho_pt = '''

LOSS no 🔴! Jogar mais Tarde 🚨

'''

texto_entrada_azul_pt = f'''

⬛ENTRADA CONFIRMADA⬛
♠️Cards:FootBall Studio
🃏Apostar na Cor:🔵
🚨Cubra o Empate
    
👉<a href='{link_convite}'>{mensagem_convite}</a>

    '''


texto_win_azul_pt = '''

GREEN! RECEBA! 🔵

'''

texto_martingale_azul_pt = '''

🚨O ideal é Fazer um Maximo de 2 Gales: 🔵

'''

texto_loss_azul_pt = '''

LOSS no 🔵! Jogar mais Tarde 🚨

'''



#TEXTOS EM ESPANHOL



texto_entrada_vermelho_esp ='''

⬛ENTRADA CONFIRMADA⬛
♠️Tarjetas:FootBall Studio
🃏Apuesta por el color:🔴
🚨Cubre el SORTEO

👉<a href='https://www.afun.com/game/101803096/Football-Studio'>Entra en la habitación</a>
    
'''


texto_win_vermelho_esp = '''

GREEN! RECIBIR! 🔴

'''

texto_martingale_vermelho_esp = '''

🚨A Lo ideal es hacer un máximo de 2 gales: 🔴

'''


texto_loss_vermelho_esp = '''

¡Loss! jugar mas tarde 🚨

'''

texto_entrada_azul_esp = '''

⬛ENTRADA CONFIRMADA⬛
♠️Tarjetas:FootBall Studio
🃏Apuesta por el color:🔵
🚨Cubre el SORTEO

👉<a href='https://www.afun.com/game/101803096/Football-Studio'>Entra en la habitación</a>

    '''


texto_win_azul_esp = '''

GREEN! RECIBIR! 🔵

'''

texto_martingale_azul_esp = '''

🚨A Lo ideal es hacer un máximo de 2 gales: 🔵

'''

texto_loss_azul_esp = '''

¡Loss! jugar mas tarde 🚨

'''


#TEXTOS EM INGLÊS


texto_entrada_vermelho_ing ='''

⬛CONFIRMED ENTRY⬛
♠️Cards:FootBall Studio
🃏Bet on color:🔴
🚨Cover the GIVEAWAY

👉<a href='https://www.afun.com/game/101803096/Football-Studio'>Join The Game</a>
    
'''


texto_win_vermelho_ing = '''

GREEN! RECEBA! 🔴

'''

texto_martingale_vermelho_ing = '''

🚨The ideal is to make a maximum of 2 gale: 🔴

'''


texto_loss_vermelho_ing = '''

 loss! play later 🚨

'''

texto_entrada_azul_ing = '''

⬛CONFIRMED ENTRY⬛
♠️Cards:FootBall Studio
🃏Bet on color:🔵
🚨Cover the GIVEAWAY

👉<a href='https://www.afun.com/game/101803096/Football-Studio'>Join The Game</a>
    '''


texto_win_azul_ing = '''

GREEN! RECEBA! 🔵

'''

texto_martingale_azul_ing = '''

🚨The ideal is to make a maximum of 2 gale: 🔵

'''

texto_loss_azul_ing = '''

loss! play later 🚨

'''








while True: 
    print('loop1')
    while True:
        print('loop2')
        try:
            service = Service('./chromedriver.exe')

            driver = webdriver.Chrome(service=service)

            driver.get("https://www.afun.com/game/101803096/Football-Studio")

            element = WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[2]/div[1]/input'))
            )
        except: 
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            break


        try:
            sleep(tempo1)

            driver.find_element(By.XPATH, '//*[@id="app"]/div[6]/button').click()


            sleep(tempo1)

            driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[2]/div[1]/input').send_keys(user)

            sleep(tempo1)

            driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[2]/div[3]/form/input').send_keys(senha)

            sleep(tempo1)

            driver.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div[2]/div[2]/button').click()

        except: 
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            break
            


        try:
            roleta = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[6]/div/img'))
            )

        except:pass

        if roleta:
            sleep(tempo1)
            driver.find_element(By.XPATH, '//*[@id="app"]/div[6]/div/img').click()
            sleep(tempo2)


        driver.execute_script("window.open('https://skylinescore0003.evo-games.com/frontend/evo/r2/#category=all_games&game=topcard&table_id=TopCard000000001&lobby_launch_id=a410769d91c647a881ccdcf7194fd28c', 'new_window')")
        driver.switch_to.window(driver.window_handles[1])

        sleep(tempo2)



        try:
            erro = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[9]/div/div'))
            )
        except:
            erro = False
            pass



        while True:
            erros = ''
    
            try: 
                expired = WebDriverWait(driver, 1).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[9]/div/div'))
                            )

                expired = True
                    

            except:
                expired = False
                pass
        
            try: 
                inativo = WebDriverWait(driver, 1).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[9]/div[1]/button/span'))
                            )

                inativo = True
    

            except:
                inativo = False
                pass

            try:

                if erro:
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    driver.close()
                    break
                
                if expired == True:
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    driver.close()
                    break
                    


                if inativo == True:
                    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[9]/div[2]').click()
                    inativo == False
                else: 
                    try: 
                        
                        cores1 = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[6]/div/div[3]/div/div/div/div[1]'))
                            )
                                             
                        cor1= cores1.text
                        confirmado = False
                       
                    except:
                        confirmado = True
                        pass

                    if confirmado == True:
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        driver.close()
                        break
                    
#sep
                    try: 
                        sleep(1)
                        cores1s = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[6]/div/div[3]/div/div/div/div[1]'))
                            )
                                             
                        cor1s= cores1s.text
                       
                    except:
                        pass 



                    if cor1 != cor1s:
                        cores1 = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[6]/div/div[3]/div/div/div/div[1]'))
                            )
                                             
                        cor1 = cores1.text
                       


                    erros = cor1
                    if erros != cor1:               
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        driver.close()
                        break
        

                    try: 
                        
                        cores2 = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[6]/div/div[3]/div/div/div/div[2]'))
                            ) 
                        cor2= cores2.text

                    except:
                        
                        pass 
                        
                    


                    try: 
                        
                        cores3 = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[6]/div/div[3]/div/div/div/div[3]'))
                            ) 
                        cor3 = cores3.text
                        

                    except:
                        
                        pass 
                    
                        
                    try: 
                        
                        cores4 = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[6]/div/div[3]/div/div/div/div[4]'))
                            )             
                        cor4= cores4.text

                    except:
                        
                       pass 
                        


                    try: 
                        
                        cores5 = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[6]/div/div[3]/div/div/div/div[5]'))
                            ) 
                        cor5= cores5.text
                        
                    
                    except:    
                        pass 


                    try: 
                        
                        cores6 = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[6]/div/div[3]/div/div/div/div[6]'))
                            ) 
                        cor6= cores6.text
                    
                        
                    except:
                        
                        pass 


                    try: 
                        
                        cores7 = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[6]/div/div[3]/div/div/div/div[7]'))
                            ) 
                        cor7= cores7.text
                    
                        
                    except:
                        
                        pass 


                    try: 
                        
                        cores8 = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[6]/div/div[3]/div/div/div/div[8]'))
                            ) 
                        cor8 = cores8.text
                        
                        
                    
                        
                    except:
                        
                        pass 


                    try: 
                        
                        cores9 = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[6]/div/div[3]/div/div/div/div[9]'))
                            ) 
                        cor9 = cores9.text
                    
                        
                    except:
                        pass 


                 
                    lista_cores.append(cor1)
                    lista_cores.append(cor2)
                    lista_cores.append(cor3)
                    lista_cores.append(cor4)
                    lista_cores.append(cor5)
                    lista_cores.append(cor6)
                    lista_cores.append(cor7)
                    lista_cores.append(cor8)
                    lista_cores.append(cor9)



                    if lista_cores[0:5] == ['A', 'A', 'A', 'A', 'H'] or lista_cores[0:5] == ['A', 'A', 'A', 'A', 'D']:                   
                        lista_cores.clear()
                        texto = f'''

        {texto_entrada_vermelho_pt}

        '''
                        texto_esp = f'''
        {texto_entrada_vermelho_esp}

                        '''
                        texto_ing = f'''
        {texto_entrada_vermelho_ing}
                        '''
                        if texto != texto_atual and texto != texto_atual2:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={texto}'
                            result = requests.get(url_base)
                            texto_atual2 = texto
                            

                        else:
                            
                            pass

                        if texto_esp != texto_atual_esp and texto_esp != texto_atual2_esp:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_esp}&parse_mode=HTML&text={texto_esp}'
                            result = requests.get(url_base)
                            texto_atual2_esp = texto_esp
                            

                        else:
                            
                            pass

                        if texto_ing != texto_atual_ing and texto_ing != texto_atual2_ing:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_ing}&parse_mode=HTML&text={texto_ing}'
                            result = requests.get(url_base)
                            texto_atual2_ing = texto_ing
                            

                        else:
                            
                            pass

                    elif lista_cores[0:6] == ['D','A', 'A', 'A', 'A', 'H'] or lista_cores[0:6] == ['D','A', 'A', 'A', 'A', 'D'] or lista_cores[0:6] == ['H','A', 'A', 'A', 'A', 'H'] or lista_cores[0:6] == ['H','A', 'A', 'A', 'A', 'D'] or lista_cores[0:7] == ['H','A','A', 'A', 'A', 'A', 'H'] or lista_cores[0:7] == ['H','A','A', 'A', 'A', 'A', 'D'] or lista_cores[0:7] == ['D','A','A', 'A', 'A', 'A', 'H'] or lista_cores[0:7] == ['D','A','A', 'A', 'A', 'A', 'D'] or lista_cores[0:8] == ['H','A','A','A', 'A', 'A', 'A', 'H'] or lista_cores[0:8] == ['H','A','A','A', 'A', 'A', 'A', 'D'] or lista_cores[0:8] == ['D','A','A','A', 'A', 'A', 'A', 'H'] or lista_cores[0:8] == ['D','A','A','A', 'A', 'A', 'A', 'D']:
                        
                        lista_cores.clear()
                        texto = f'''
        {texto_win_vermelho_pt}
        '''
                        texto_esp = f'''
        {texto_win_vermelho_esp}

                        '''
                        texto_ing = f'''
        {texto_win_vermelho_ing}
                        '''            
                        if texto != texto_atual and texto != texto_atual2:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                            result = requests.get(url_base)
                            texto_atual2 = texto
                            wins +=1
                            print(f'wins: {wins}')
                            print(f'loss: {loss}')
                            

                        else:
                            
                            pass

                        if texto_esp != texto_atual_esp and texto_esp != texto_atual2_esp:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_esp}&parse_mode=HTML&text={texto_esp}'
                            result = requests.get(url_base)
                            texto_atual2_esp = texto_esp
                            

                        else:
                            
                            pass

                        if texto_ing != texto_atual_ing and texto_ing != texto_atual2_ing:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_ing}&parse_mode=HTML&text={texto_ing}'
                            result = requests.get(url_base)
                            texto_atual2_ing = texto_ing
                            

                        else:
                            
                            pass


                    elif lista_cores[0:6] == ['A','A', 'A', 'A', 'A', 'H'] or lista_cores[0:6] == ['A','A', 'A', 'A', 'A', 'D']:
                        
                        lista_cores.clear()
                        texto = f'''

        {texto_martingale_vermelho_pt}

        '''
                        texto_esp = f'''
        {texto_martingale_vermelho_esp}

                        '''
                        texto_ing = f'''
        {texto_martingale_vermelho_ing}
                        '''
                        if texto != texto_atual and texto != texto_atual2:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                            result = requests.get(url_base)
                            texto_atual2 = texto
                            

                        else:
                            
                            pass
                        if texto_esp != texto_atual_esp and texto_esp != texto_atual2_esp:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_esp}&parse_mode=HTML&text={texto_esp}'
                            result = requests.get(url_base)
                            texto_atual2_esp = texto_esp
                            

                        else:
                            
                            pass

                        if texto_ing != texto_atual_ing and texto_ing != texto_atual2_ing:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_ing}&parse_mode=HTML&text={texto_ing}'
                            result = requests.get(url_base)
                            texto_atual2_ing = texto_ing
                            

                        else:
                            
                            pass

                    elif lista_cores[0:8] == ['A','A','A','A', 'A', 'A', 'A', 'H'] or lista_cores[0:8] == ['A','A','A','A', 'A', 'A', 'A', 'D']:
                        
                        lista_cores.clear()
                        
                        texto = f'''
                        
        {texto_loss_vermelho_pt}
        '''
                        texto_esp = f'''
        {texto_loss_vermelho_esp}

                        '''
                        texto_ing = f'''
        {texto_loss_vermelho_ing}
                        '''
                        if texto != texto_atual and texto != texto_atual2:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                            result = requests.get(url_base)
                            texto_atual2 = texto
                            loss +=1
                            print(f'wins: {wins}')
                            print(f'loss: {loss}')

                        else:
                            
                            pass
                        if texto_esp != texto_atual_esp and texto_esp != texto_atual2_esp:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_esp}&parse_mode=HTML&text={texto_esp}'
                            result = requests.get(url_base)
                            texto_atual2_esp = texto_esp
                            
                        else:
                            
                            pass

                        if texto_ing != texto_atual_ing and texto_ing != texto_atual2_ing:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_ing}&parse_mode=HTML&text={texto_ing}'
                            result = requests.get(url_base)
                            texto_atual2_ing = texto_ing
                            
                        else:
                            
                            pass



                    elif lista_cores[0:5] == ['H', 'H', 'H', 'H','A'] or lista_cores[0:5] == ['H', 'H', 'H', 'H','D']:
                        lista_cores.clear()
                        texto = f'''
        {texto_entrada_azul_pt}
        '''
                        texto_esp = f'''
        {texto_entrada_azul_esp}

                        '''
                        texto_ing = f'''
        {texto_entrada_azul_ing}
                        '''
                        if texto != texto_atual and texto != texto_atual2:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={texto}'
                            result = requests.get(url_base)
                            texto_atual2 = texto
                            

                        else:
                            
                            pass
                        if texto_esp != texto_atual_esp and texto_esp != texto_atual2_esp:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_esp}&parse_mode=HTML&text={texto_esp}'
                            result = requests.get(url_base)
                            texto_atual2_esp = texto_esp
                            

                        else:
                            
                            pass

                        if texto_ing != texto_atual_ing and texto_ing != texto_atual2_ing:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_ing}&parse_mode=HTML&text={texto_ing}'
                            result = requests.get(url_base)
                            texto_atual2_ing = texto_ing
                            

                        else:
                            
                            pass



                    elif lista_cores[0:6] == ['A','H', 'H', 'H', 'H', 'A'] or lista_cores[0:6] == ['A','H', 'H', 'H', 'H', 'D'] or lista_cores[0:6] == ['D','H', 'H', 'H', 'H', 'A'] or lista_cores[0:6] == ['D','H', 'H', 'H', 'H', 'D'] or lista_cores[0:7] == ['A','H','H', 'H', 'H', 'H', 'A'] or lista_cores[0:7] == ['A','H','H', 'H', 'H', 'H', 'D'] or lista_cores[0:7] == ['D','H','H', 'H', 'H', 'H', 'A'] or lista_cores[0:7] == ['D','H','H', 'H', 'H', 'H', 'D'] or lista_cores[0:8] == ['A','H','H','H', 'H', 'H', 'H', 'A'] or lista_cores[0:8] == ['A','H','H','H', 'H', 'H', 'H', 'D'] or lista_cores[0:8] == ['D','H','H','H', 'H', 'H', 'H', 'A'] or lista_cores[0:8] == ['D','H','H','H', 'H', 'H', 'H', 'D']:
                        
                        lista_cores.clear()
                        
                        texto = f'''
        {texto_win_azul_pt}
        '''
                        texto_esp = f'''
        {texto_win_azul_esp}

                        '''
                        texto_ing = f'''
        {texto_win_azul_ing}
                        '''
                        if texto != texto_atual and texto != texto_atual2:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                            result = requests.get(url_base)
                            texto_atual2 = texto
                            wins +=1
                            print(f'wins: {wins}')
                            print(f'loss: {loss}')

                        else:
                            
                            pass
                        if texto_esp != texto_atual_esp and texto_esp != texto_atual2_esp:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_esp}&parse_mode=HTML&text={texto_esp}'
                            result = requests.get(url_base)
                            texto_atual2_esp = texto_esp
                            

                        else:
                            
                            pass

                        if texto_ing != texto_atual_ing and texto_ing != texto_atual2_ing:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_ing}&parse_mode=HTML&text={texto_ing}'
                            result = requests.get(url_base)
                            texto_atual2_ing = texto_ing
                            

                        else:
                            
                            pass




                    elif lista_cores[0:6] == ['H','H', 'H', 'H', 'H', 'A'] or lista_cores[0:6] == ['H','H', 'H', 'H', 'H', 'D']:
                        lista_cores.clear()
                        texto = f'''
        {texto_martingale_azul_pt}
            '''
                        texto_esp = f'''
        {texto_martingale_azul_esp}

                        '''
                        texto_ing = f'''
        {texto_martingale_azul_ing}
                        '''
                        if texto != texto_atual and texto != texto_atual2:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                            result = requests.get(url_base)
                            texto_atual2 = texto
                            

                        else:
                            
                            pass
                        if texto_esp != texto_atual_esp and texto_esp != texto_atual2_esp:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_esp}&parse_mode=HTML&text={texto_esp}'
                            result = requests.get(url_base)
                            texto_atual2_esp = texto_esp
                            

                        else:
                            
                            pass

                        if texto_ing != texto_atual_ing and texto_ing != texto_atual2_ing:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_ing}&parse_mode=HTML&text={texto_ing}'
                            result = requests.get(url_base)
                            texto_atual2_ing = texto_ing
                            

                        else:
                            
                            pass




                    elif lista_cores[0:8] == ['H','H','H','H', 'H', 'H', 'H', 'A'] or lista_cores[0:8] == ['H','H','H','H', 'H', 'H', 'H', 'D']:
                        
                        lista_cores.clear()
                        
                        texto = f'''
        {texto_loss_azul_pt}
        '''
                        texto_esp = f'''
        {texto_loss_azul_esp}

                        '''
                        texto_ing = f'''
        {texto_loss_azul_ing}
                        '''
                        if texto != texto_atual and texto != texto_atual2:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={texto}'
                            result = requests.get(url_base)
                            texto_atual2 = texto
                            loss +=1
                            print(f'wins: {wins}')
                            print(f'loss: {loss}')

                        else:
                            
                            pass

                        if texto_esp != texto_atual_esp and texto_esp != texto_atual2_esp:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_esp}&parse_mode=HTML&text={texto_esp}'
                            result = requests.get(url_base)
                            texto_atual2_esp = texto_esp
                            

                        else:
                            
                            pass

                        if texto_ing != texto_atual_ing and texto_ing != texto_atual2_ing:
                            url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id_ing}&parse_mode=HTML&text={texto_ing}'
                            result = requests.get(url_base)
                            texto_atual2_ing = texto_ing
                            

                        else:
                            
                            pass
                    
                    
                    lista_cores.clear()

            except:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                driver.close()
                break