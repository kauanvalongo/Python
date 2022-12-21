from datetime import date
idade = int(input('Qual a idade do atleta?'))
data = date.today().year
tempo = data - idade
ano = data - tempo
if ano <= 9:
    print('Atletas com {} anos ou abaixo estão na categoria [ MIRIM ].'.format(ano))
elif ano >= 14:
    print('Atletas com {} anos estão na categoria [ INFANTIL ].'.format(ano))
elif ano == 19:
    print('Atletas com {} anos estão na categoria [ JÚNIOR ]'.format(ano))
elif ano == 20:
    print('Atletas com {} anos estão na categoria [ SÊNIOR ]'.format(ano))
elif ano > 20:
    print('Atletas com {} anos ou acima estão na categoria [ MASTER ]'.format(ano))
