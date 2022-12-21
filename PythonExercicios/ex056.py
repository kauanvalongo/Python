nomevelho = ''
media = 0
feminino = 0
velho = 0
homem = 0
for i in range(1 , 5):
    print(f'----- Pessoa {i} ------')
    nome = str(input('Nome:'))
    sexo = str(input('Sexo: [F/[M]')).upper()
    idade = int(input('Idade:'))
    if idade > 0:
        media += idade
    if idade < 20 and sexo == 'F':
        feminino += 1
    if i == 1 and sexo == 'M':
        velho = idade
        nomevelho = nome
    else:
        if idade > velho and sexo == 'M':
           velho = idade
           nomevelho = nome
print(f'Média de Idade Das Pessoas: {media/4}')
print(f'O Nome do Homem Mais Velho é {nomevelho} e Ele Tem {velho} Anos.')
print(f'E EXATAMENTE {feminino} mulheres têm menos de 20 anos.')
