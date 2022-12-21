extenso = 'zero', 'um' , 'dois' , 'três' , 'quatro' , 'cinco' , 'seis' , 'sete' , 'oito' , 'nove' , 'dez' , 'onze' , 'doze' , 'treze' , 'quatorze' , 'quinze' , 'dezesseis', 'dezessete' , 'dezoito' , 'dezenove' , 'vinte'
num = ''
while num not in (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21):
    num = int(input('Digite Um valor entre 0 e 20: '))
for c in extenso[num]:
    print(c, end='')
