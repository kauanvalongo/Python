v = int(input('Qual o valor do produto? R$'))
d = int(input('Quanto você quer de desconto?'))
r = v - (v*d/100)
print('Seu produto que custava {} agora com o desconto de {}% está saido por {}'.format(v,d,r))