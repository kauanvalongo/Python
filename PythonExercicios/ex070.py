total = maismil = 0
nomebarato = ''
precobarato = 0
c = 0
print('-='*20)
print('MERCADÃO DOS SUPREMACISTAS')
print('-='*20)
while True:
    nome = str(input('Qual o Nome do Produto? '))
    preco = int(input('Qual o preço do produto? R$'))
    total += preco
    c += 1
    if preco > 1000:
        maismil += 1
    if c == 1:
        precobarato = preco
        nomebarato = nome
    else:
        if preco < precobarato:
            precobarato = preco
            nomebarato=nome
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja Adicionar Outro Produto? [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'O total da compra foi de {total}')
print(f'Temos {maismil} produtos valendo mais que mil Reais')
print(f'O nome do produto mais barato é: {nomebarato} que custa: R${precobarato}')
