import datetime


def voto(num):
    from datetime import date
    ano = date.today().year - num
    if ano < 16:
        return f'A pessoa tem {ano} anos... VOTO NEGADO.'
    elif 18 > ano or ano > 65:
        return f'A pessoa tem {ano} anos... VOTO OPCIONAL.'
    elif 18 <= ano <= 65:
        return f'A pessoa tem {ano} anos... VOTO OBRIGATÓRIO.'


data = int(input('Em que ano a pessoa nasceu?? : '))
print(voto(data))