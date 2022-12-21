import random
from time import sleep
c = random.randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('-=-'*20)
j = int(input('Tente acertar o numero que eu pensei!'))
print('PROCESSANDO...')
sleep(3)
if j == c :
    print('Uau! você tem sorte!')
else:
    print('ERROU!')
print('O número correto é {}'.format(c))
