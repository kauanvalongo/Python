import requests
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from datetime import datetime

horarios = [
'00:10','00:11','00:12','00:13','00:14','00:16','00:17','00:18','00:19','00:20',

'00:35','00:36','00:37','00:38','00:39','00:42','00:43','00:44','00:45','00:46',

'01:05','01:06','01:07','01:08','01:09','01:11','01:12','01:13','01:14','01:15',

'01:36','01:37','01:38','01:39','01:40','01:43','01:44','01:45','01:46','01:47',
            
'01:53','01:54','01:55','01:56','01:57','02:00','02:01','02:02','02:03','02:04',

'02:26','02:27','02:28','02:29','02:30','02:33','02:34','02:35','02:36','02:37',

'02:37','02:38','02:39','02:40','02:41','02:44','02:45','02:46','02:47','02:48',

'03:37','03:36','03:39','03:40','03:41','03:44','03:45','03:46','03:47','03:48',

'03:56','03:57','03:58','03:59','04:00','04:03','04:04','04:05','04:06','04:07',

'04:10','04:11','04:12','04:13','04:14','04:17','04:18','04:19','04:20','04:21',

'04:23','04:24','04:25','04:26','04:27','04:30','04:31','04:32','04:33','04:34',

'04:36','04:37','04:38', '04:39','04:40','04:43','04:44','04:45','04:46','04:47',

'04:55','04:56','04:57','04:58','04:59','05:02','05:03','05:04','05:05','05:06',

'05:40','05:41','05:42','05:43','05:44','05:47','05:48','05:49','05:50','05:51',

'05:56','05:57','05:58','05:59','06:00','06:03','06:04','06:05','06:06','06:07',

'06:16','06:17','06:18','06:19','06:20','06:23','06:24','06:25','06:26','06:27',

'06:56','06:57','06:58','06:59','07:00','07:03','07:04','07:05','07:06','07:07',

'07:20','07:21','07:22','07:23','07:24','07:27','07:28','07:29','07:30','07:31',

'07:46','07:47','07:48','07:49','07:50','07:53','07:54','07:55','07:56','07:57',

'08:20','08:21','08:22','08:23','08:24','08:27','08:28','08:29','08:30','08:31',

'08:37','08:38','08:39','08:40','08:41','08:43','08:44','08:45','08:46','08:47',

'09:00','09:01','09:02','09:03','09:04','09:08','09:09','09:10','09:11','09:12',

'09:20','09:21','09:22','09:23','09:24','09:27','09:28','09:29','09:30','09:31',

'09:40','09:41','09:42','09:43','09:44','09:47','09:48','09:49','09:50','09:51',

'09:55','09:56','09:57','09:58','09:59','10:01','10:02','10:03','10:04','10:05',

'10:10','10:11','10:12','10:13','10:14','10:17','10:18','10:19','10:20','10:21',

'10:37','10:38','10:39','10:40','10:41','10:44','10:45','10:46','10:47','10:48',

'10:50','10:51','10:52','10:53','10:54','10:57','10:58','10:59','11:00','11:01',

'11:20','11:21','11:22','11:23','11:24','11:27','11:28','11:29','11:30','11:31',

'11:42','11:43','11:44','11:45','11:46','11:50','11:51','11:52','11:53','11:54',

'12:00','12:01','12:02','12:03','12:04','12:07','12:08','12:09','12:10','12:11',

'12:17','12:18','12:19','12:20','12:21','12:24','12:25','12:26','12:27','12:28',

'12:34','12:35','12:36','12:37','12:38','12:41','12:42','12:43','12:44','12:45',

'12:47','12:48','12:49','12:50','12:51','12:54','12:55','12:56','12:57','12:58',

'13:04','13:05','13:06','13:07','13:08','13:09','13:10','13:11','13:12','13:13',

'13:16','13:17','13:18','13:19','13:20','13:23','13:24','13:25','13:26','13:27',

'13:37','13:38','13:39','13:40','13:41','13:43','13:44','13:45','13:46','13:47',

'14:00','14:01','14:02','14:03','14:04','14:07','14:08','14:09','14:10','14:11',

'14:34','14:35','14:36','14:37','14:38','14:41','14:42','14:43','14:44','14:45',

'14:48','14:49','14:50','14:51','14:52','14:55','14:56','14:57','14:58','14:59',

'15:04','15:05','15:06','15:07','15:08','15:11','15:12','15:13','15:14','15:15',

'15:16','15:17','15:18','15:19','15:20','15:23','15:24','15:25','15:26','15:27',

'15:28','15:29','15:30','15:31','15:32','15:35','15:36','15:37','15:38','15:39',

'16:10','16:11','16:12','16:13','16:14','16:17','16:18','16:19','16:20','16:21',

'16:32','16:33','16:34','16:35','16:36','16:40','16:41','16:42','16:43','16:44',

'17:06','17:07','17:08','17:09','17:10','17:14','17:15','17:16','17:17','17:18',

'17:20','17:21','17:22','17:23','17:24','17:27','17:28','17:29','17:30','17:31',

'17:47','17:48','17:49','17:50','17:51','17:54','17:55','17:56','17:57','17:58',

'18:05','18:06','18:07','18:08','18:09','18:11','18:12','18:13','18:14','18:15',

'18:26','18:27','18:28','18:29','18:30','18:33','18:34','18:35','18:36','18:37',

'18:40','18:41','18:42','18:43','18:44','18:47','18:48','18:49','18:50','18:51',

'19:07','19:08','19:09','19:10','19:11','19:14','19:15','19:16','19:17','19:18',

'19:36','19:37','19:38','19:39','19:40','19:43','19:44','19:45','19:46','19:47',

'19:53','19:54','19:55','19:56','19:57','20:00','20:01','20:02','20:03','20:04',

'20:05','20:06','20:07','20:08','20:09','20:12','20:13','20:14','20:15','20:16',

'20:22','20:23','20:24','20:25','20:26','20:30','20:31','20:32','20:33','20:34',

'20:37','20:38','20:39','20:40','20:41','20:44','20:45','20:46','20:47','20:48',

'21:00','21:01','21:02','21:03','21:04','21:07','21:08','21:09','21:10','21:11',

'21:27','21:28','21:29','21:30','21:31','21:34','21:35','21:36','21:37','21:38',

'21:47','21:48','21:49','21:50','21:51','21:52','21:53','21:54','21:55','21:56',

'21:50','21:51','21:52','21:53','21:54','21:57','21:58','21:59','22:00','22:01', 

'22:05','22:06','22:07','22:08','22:09','22:11','22:12','22:13','22:14','22:15',

'22:17','22:18','22:19','22:20','22:21','22:23','22:24','22:25','22:26','22:27',

'23:03','23:04','23:05','23:06','23:07','23:10','23:11','23:12','23:13','23:14',

'23:27','23:28','23:29','23:30','23:31','23:34','23:35','23:36','23:37','23:38', 

'23:32','23:33','23:34','23:35','23:36','23:40','23:41','23:42','23:43','23:44',

'23:50','23:51','23:52','23:53','23:54','23:57','23:58','23:59','00:00','00:01',

        ]

certeiro = ['00:10','00:20','00:35','00:39','01:05','01:15','01:36','01:47','01:53','02:04','02:26','02:30','02:33','02:48','03:37','03:48','03:56','04:07','04:10','04:21','04:23','04:34','04:36','04:47','04:55','05:06','05:40','05:51','05:56','06:07','06:16','06:27','06:56','07:07','07:46','07:57','08:20','08:31','08:37','08:47','09:00','09:12','09:20','09:31','09:40','09:51','10:10','10:21','10:37','10:48','10:50','11:01','11:20','11:31','11:42','11:54','12:00','12:11','12:17','12:28','12:34','12:45','12:47','12:58','13:37','13:47','14:00','14:11','14:34','14:45','14:48','14:59','15:04','15:15','15:16','15:27','15:28','15:39','16:10','16:21','16:32','16:44','17:06','17:18','17:20','17:31','17:47','17:58','18:05','18:15','18:26','18:37','18:40','18:51','19:07','19:18','19:36','19:47','19:53','20:04','20:05','20:16','20:22','20:34','20:37','20:48','21:27','21:38','21:47','21:56','22:01','22:15','22:17','22:27','23:03','23:14','23:27','23:44','23:50',
            
'00:01','00:16','01:09','01:40','01:43','01:57','02:00','02:33','02:44','04:03','04:17','04:30','04:43','05:02','05:47','06:03','06:23','07:03','08:27','08:43','09:08','00:14','00:42','00:46','01:09','01:40','01:57','02:30','02:42','03:41','03:44','04:00','04:14','04:27','04:40','04:59','05:44','06:00','06:20','07:00','07:50','08:24','08:41','09:04','09:24','09:27','09:44','09:47','10:14','10:17','10:41','10:44','10:54','10:57','11:24','11:27','11:46','11:50','12:04','12:07','12:21','12:24','12:38','12:41','12:51','12:54','13:41','13:43','14:04','14:07','14:38','14:41','14:52','14:55','15:08','15:11','15:20','15:23','15:32','15:35','16:14','16:17','17:10','17:14','17:24','17:27','17:51','17:54','18:09','18:11','18:30','18:33','18:44','18:47','19:11','19:14','19:40','19:43','19:57','20:00','20:09','20:12','20:26','20:30','20:41','20:44','21:31','21:34','21:51','21:52','21:57','22:09','22:11','22:05','22:21','22:23','23:07','23:10','23:31','23:34','23:36','23:40','23:54','23:57','16:38','16:41','02:41','02:44','07:31','07:20','07:24','07:27','16:36','16:40','10:05','09:55','09:59','10:01', '13:04','13:08','13:09','13:13','13:16','13:20','13:23','13:27',
            ]

red = ['00:21','01:16','01:48','02:05','02:38','02:49','03:49','04:08','04:22','04:35','04:48','05:07','05:52','06:08','06:28','07:08','07:58','08:32','08:48','09:13','09:32','09:52','10:22','10:49','11:02','11:32','11:55','12:12','12:29','12:46','12:59','13:48','14:12','14:46','13:00','15:16','15:28','15:40','16:22','16:45','17:19','17:32','17:59','18:16','18:38','18:52','19:19','19:48','20:05','20:17','20:35','20:49','21:39','21:57','22:02','22:16','22:28','23:15','23:39','23:45','00:02','10:06','13:14','13:28','21:00','21:04','21:07','21:11',
            ]

token = '5468560434:AAE11S9PQhsDHzBnrEvbT8K-IOUniPSBbY8'
chat_id = '-905124813'

texto = ''
texto_atual = ''
texto_atual2 = ''

pegar_id_sinal = ''
sinal = ''
text = ''
text_atual = ''
text_atual2 = ''

loss = 0
win = 0

a = ''
cf = False
ch = False
pa = False 
ct = False

sinais = True

link_token = 'https://tracksino.com/crazytime'
service = Service('./chromedriver.exe')
service.command_line_args()[:] = [
        '--disable-extensions',  # Desativar extensões do Chrome
        '--disable-gpu',  # Desativar aceleração de GPU     
    ]
options = Options()
options.add_argument(f"--window-size={1920},1080")
options.add_argument(f"--headless")
driver = webdriver.Chrome(options=options)
driver.get(f"{link_token}")
while True:
    if loss < 0:
        loss = 0
    if loss > 3:
        loss = 3

    if loss == 3:
          sinais = False

    if loss == 0:
          sinais = True


    hora = datetime.now()
    hora = hora.strftime("%H:%M")
    if sinais == True:
          
        if hora == '00:02':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 00:12 e 00:19

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 00:37 e 00:44

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 01:07 e 01:13

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 01:38 e 01:45

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                text_atual2 = text


        elif hora == '01:30':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 01:55 e 02:02

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 02:28 e 02:35

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 02:39 e 02:46

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑
        
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 03:39 e 03:46

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                
                                text_atual2 = text
                                

        elif hora == '03:49':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 03:58 e 04:05

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 04:12 e 04:19

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 04:25 e 04:32

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑
        
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 04:38 e 04:45

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                text_atual2 = text

        elif hora == '04:48':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 04:57 e 05:04

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 05:42 e 05:49

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 05:58 e 06:05

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑
        
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 06:18 e 06:25

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                print('este é o id: ',pegar_id_sinal)
                                text_atual2 = text

        elif hora == '06:40':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 06:58 e 07:05

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 07:22 e 07:29

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 07:48 e 07:55

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑
        
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 08:22 e 08:29

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                print('este é o id: ',pegar_id_sinal)
                                text_atual2 = text

        elif hora == '08:32':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 08:39 e 08:45

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 09:02 e 09:10

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 09:22 e 09:29

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑
        
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 09:42 e 09:49

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 09:57 e 10:03

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                print('este é o id: ',pegar_id_sinal)
                                text_atual2 = text

        elif hora == '09:55':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 10:12 e 10:19

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 10:39 e 10:46

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 10:52 e 10:59

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑
        
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 11:22 e 11:29

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                print('este é o id: ',pegar_id_sinal)
                                text_atual2 = text

        elif hora == '11:33':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 11:44 e 11:52

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 12:02 e 12:09

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 12:19 e 12:26

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑
        
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 12:36 e 12:43

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                print('este é o id: ',pegar_id_sinal)
                                text_atual2 = text


        elif hora == '12:45':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 12:49 e 12:56

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 13:06 e 13:11

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 13:18 e 13:25

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 13:39 e 13:45

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 14:02 e 14:09

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑
        
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 14:36 e 14:43

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                print('este é o id: ',pegar_id_sinal)
                                text_atual2 = text


        elif hora == '14:45':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 14:50 e 14:57

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 15:06 e 15:13

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 15:18 e 15:25

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑
        
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 15:30 e 15:37

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                print('este é o id: ',pegar_id_sinal)
                                text_atual2 = text

        elif hora == '15:45':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 16:12 e 16:19

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 16:34 e 16:42

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 17:08 e 17:16

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑
        
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 17:22 e 17:29

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                print('este é o id: ',pegar_id_sinal)
                                text_atual2 = text

        elif hora == '17:35':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 17:49 e 17:56

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 18:07 e 18:13

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 18:28 e 18:35

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑
        
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 18:42 e 18:49

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                print('este é o id: ',pegar_id_sinal)
                                text_atual2 = text

        elif hora == '18:55':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 19:09 e 19:16

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 19:38 e 19:45

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 19:55 e 20:02(risco alto)

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑
        
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 20:07 e 20:14

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                print('este é o id: ',pegar_id_sinal)
                                text_atual2 = text

        elif hora == '20:17':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 20:24 e 20:32

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 20:39 e 20:46

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 21:02 e 21:09

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 21:29 e 21:36

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑
        
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 21:49 e 21:54

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 21:52 e 21:59

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                print('este é o id: ',pegar_id_sinal)
                                text_atual2 = text


        elif hora == '22:00':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 22:07 e 22:13

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 22:19 e 22:25

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 21:29 e 21:36

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑
        
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 23:05 e 23:12

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                print('este é o id: ',pegar_id_sinal)
                                text_atual2 = text

        elif hora == '23:15':
            text = """
⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 23:29 e 23:36

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 23:34 e 23:42

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑

⚫⚠️ATENÇÃO⚠️⚫

ROLETA: Crazy Time

🕰️HORÁRIOS: 23:52 e 23:59

Entre:
1 minuto antes
1 minuto depois

Aposte no:
Coin Flip🔴🔵
Cash Hunt🎯
Pachinko🏵️
Crazy Time🔑
        
⚫⚠️ATENÇÃO⚠️⚫

            """
            if sinal != text:  
                try:
                    url_base = f'https://api.telegram.org/bot{token}/deleteMessage?chat_id={chat_id}&message_id={pegar_id_sinal}'
                    result = requests.get(url_base)
                except:
                    pass
                sinal = text
            
            if text != text_atual and text != text_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={text}'
                                result = requests.get(url_base).json()
                                pegar_id_sinal = result['result']['message_id']
                                print('este é o id: ',pegar_id_sinal)
                                text_atual2 = text
    
    sleep(5)
    try:
        bonus1 = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="spin-history"]/tbody/tr[1]/td[1]'))
                )
    except:
        sleep(20)
        driver.refresh()
        continue
    
    bonus1 = bonus1.text.replace(' ', '').replace('@', '')
    print('total bonus1 ; ',bonus1)
    bonus1 = bonus1[4:]
    print('bonus atualizado :',bonus1)

    multiplier = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="spin-history"]/tbody/tr[1]/td[4]/span'))
            )
    multiplier = multiplier.text

    icone1 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="spin-history"]/tbody/tr[1]/td[3]/center/i'))
            )
    icone_class = icone1.get_attribute('class')


    try:
        elementv = driver.find_element(By.CLASS_NAME, 'crazytime-heads-icon')
        posicao = elementv.location
    except:
        pass
    try:
        elementb = driver.find_element(By.CLASS_NAME, 'crazytime-tails-icon')
        posicao = elementb.location
    except:
        pass

    if bonus1 in horarios: 
        print(bonus1)

        if icone_class == "ico-crazytime-cf":
            loss -= 1
            cf = True
            try:
                elementv = driver.find_element(By.CLASS_NAME, 'crazytime-heads-icon')
                posicao = elementv.location
                print(f'y:{posicao["y"]} - x: {posicao["x"]} ')
                elementov = True
                color = elementv.value_of_css_property('color')
            except:
                elementov = False
                pass
            try:
                elementb = driver.find_element(By.CLASS_NAME, 'crazytime-tails-icon')
                posicao = elementb.location
                print(f'y:{posicao["y"]} - x: {posicao["x"]} ')
                elementob = True
                color = elementb.value_of_css_property('color')
            except:
                elementob = False
                pass
            
            if elementov == True and elementob == True:
                print('duas cores')
                if elementv.location['y'] < elementb.location['y']:
                    print('vvvv')
                    color = elementv.value_of_css_property('color')
                else: 
                    color = elementb.value_of_css_property('color')
            
            print(color)

            if color == 'rgba(196, 11, 42, 1)':
                cor = '🔴'
            elif color == 'rgba(17, 92, 207, 1)':
                cor ='🔵'
            else:
                cor = '...'
            if bonus1 in certeiro:
                print(bonus1)
                print('coin flip não certeiro')
                print(multiplier)
                sleep(10)
                driver.refresh()
                texto = f'''
✔🧡Green não certeiro🧡✔
Quem foi na margem de 2min pegou:

{bonus1}
Coin Flip
{multiplier}{cor}
                '''
                if texto != texto_atual and texto != texto_atual2:
                        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={texto}'
                        result = requests.get(url_base).json()
                        pegar_id = result['result']['message_id']
                        print('este é o id: ',pegar_id)
                        texto_atual2 = texto
            else:
                print(bonus1)
                print('coin flip')
                print(multiplier)
                sleep(10)
                driver.refresh()
                texto = f'''
✔💚Deu Green💚✔
Pegamos:

{bonus1}
Coin Flip
{multiplier}{cor}
                '''
                if texto != texto_atual and texto != texto_atual2:
                        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={texto}'
                        result = requests.get(url_base).json()
                        pegar_id = result['result']['message_id']
                        print('este é o id: ',pegar_id)
                        texto_atual2 = texto

        elif icone_class == "ico-crazytime-ch":
            loss -= 1
            ch = True
            if bonus1 in certeiro:
                print(bonus1)
                print('cash hunt não certeiro')
                print(multiplier)
                sleep(10)
                driver.refresh()
                texto = f'''
✔🧡Green não certeiro🧡✔
Quem foi na margem de 2min pegou:

{bonus1}
Cash Hunt🎯
{multiplier}
                '''
                if texto != texto_atual and texto != texto_atual2:
                        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={texto}'
                        result = requests.get(url_base).json()
                        pegar_id = result['result']['message_id']
                        print('este é o id: ',pegar_id)
                        texto_atual2 = texto
            else:
                print(bonus1)
                print('cash hunt')
                print(multiplier)
                sleep(10)
                driver.refresh()
                texto = f'''
✔💚Deu Green💚✔
Pegamos:

{bonus1}
Cash Hunt🎯
{multiplier}
                '''
                if texto != texto_atual and texto != texto_atual2:
                        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={texto}'
                        result = requests.get(url_base).json()
                        pegar_id = result['result']['message_id']
                        print('este é o id: ',pegar_id)
                        texto_atual2 = texto

        elif icone_class == "ico-crazytime-pa":
            loss -= 1
            pa = True
            if bonus1 in certeiro:
                print(bonus1)
                print('pachinko não certeiro')
                print(multiplier)
                sleep(10)
                driver.refresh()
                texto = f'''
✔🧡Green não certeiro🧡✔
Quem foi na margem de 2min pegou:

{bonus1}
Pachinko
{multiplier}🏵️
                '''
                if texto != texto_atual and texto != texto_atual2:
                        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={texto}'
                        result = requests.get(url_base).json()
                        pegar_id = result['result']['message_id']
                        print('este é o id: ',pegar_id)
                        texto_atual2 = texto
            else:
                print(bonus1)
                print('pachinko')
                print(multiplier)
                sleep(10)
                driver.refresh()
                texto = f'''
✔💚Deu Green💚✔
Pegamos:

{bonus1}
Pachinko
{multiplier}🏵️
                '''
                if texto != texto_atual and texto != texto_atual2:
                        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={texto}'
                        result = requests.get(url_base).json()
                        pegar_id = result['result']['message_id']
                        print('este é o id: ',pegar_id)
                        texto_atual2 = texto

        elif icone_class == "ico-crazytime-ct":
            loss -= 1
            ct = True
            if bonus1 in certeiro:
                print(bonus1)
                print('crazy time não certeiro')
                print(multiplier)
                sleep(10)
                driver.refresh()
                texto = f'''
✔🧡Green não certeiro🧡✔
Quem foi na margem de 2min pegou:

{bonus1}
Crazy Time

💚    💙    💛
{multiplier}
                '''
                if texto != texto_atual and texto != texto_atual2:
                        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={texto}'
                        result = requests.get(url_base).json()
                        pegar_id = result['result']['message_id']
                        print('este é o id: ',pegar_id)
                        texto_atual2 = texto
            else:
                print(bonus1)
                print('crazy time')
                print(multiplier)
                sleep(10)
                driver.refresh()
                texto = f'''
✔💚Deu Green💚✔
Pegamos:

{bonus1}
Crazy Time

💚    💙    💛
{multiplier}
                '''
                if texto != texto_atual and texto != texto_atual2:
                        url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={texto}'
                        result = requests.get(url_base).json()
                        pegar_id = result['result']['message_id']
                        print('este é o id: ',pegar_id)
                        texto_atual2 = texto
        else:
                sleep(10)
                driver.refresh()
    else: 
        if bonus1 in red:
                if cf == True or ch == True or pa == True or ct == True:       
                    a = bonus1
                    cf = False
                    ch = False
                    pa = False 
                    ct = False
                    sleep(20)
                    driver.refresh()

                else:
                    if  a != bonus1:
                        a = bonus1
                        texto = f'''
            ❌{bonus1} : ESSE NÃO BATEU❌
                            '''
                        if texto != texto_atual and texto != texto_atual2:
                                url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=HTML&text={texto}'
                                result = requests.get(url_base).json()
                                pegar_id = result['result']['message_id']
                                print('id do chat: ',pegar_id)
                                texto_atual2 = texto
                                loss += 1
                        
                        sleep(5)
                        driver.refresh()
                    else:
                        sleep(15)
                        driver.refresh()

        else: 
            sleep(10)
            driver.refresh()
               
