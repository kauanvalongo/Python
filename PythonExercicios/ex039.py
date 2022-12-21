from datetime import date
ano = int(input('Qual foi o ano em que você nasceu?'))
atual = date.today().year
s = atual - ano
a = ano + 18
b = a - atual

if s == 18:
    print('Quem nasceu em {} está com {} anos em 2022, e deve se alistar este ano.'.format(ano,s))
elif s >= 19:
    print('Quem nasceu em {} está com {} anos em 2022. O alistamento foi à {} ano(s) em {}.'.format(ano,s,b,a))
elif s <= 17:
    print('Quem nasceu em {} está com {} anos em 2022. Ainda vai se alistar daqui à {} ano(s) em {}.'.format(ano,s,b,a))
