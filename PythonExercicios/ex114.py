import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[0;30;41mO site Não está acessível no momento...\033[m')
else:
    print('\033[0;30;42mO Site Está Acessível Atualmente!\033[m')
    
