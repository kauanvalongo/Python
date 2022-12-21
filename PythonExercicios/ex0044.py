valor = int(input('Qual é O Valor do Produto Que Deseja Comprar?'))
print(str('''Escolha Seu Método de Pagamento:
[ 1 ] - DINHEIRO/CHEQUE( 10% de desconto )
[ 2 ] -  À VISTA NO CARTÃO( 5% de desconto )
[ 3 ] - 2X NO CARTÃO ( sem desconto )
[ 4 ] - 3X OU MAIS NO CARTÃO( 20% de juros )'''))
metodo = int(input('Digite Aqui o Número Indicado ao Método Que Deseja:'))
a = valor - (valor * 10 / 100)
b = valor - (valor * 5 / 100)
c = valor
d = valor + (valor * 20 / 100)
if metodo == 1:
    print('O valor do produto com desconto ficará por {}.'.format(a))
elif metodo == 2:
    print('O valor do produto com desconto ficará por {}.'.format(b))
elif metodo == 3:
    print('O Valor do Produto Não Muda com Este Método de Pagamento. Valor: {}'.format(c))
elif metodo == 4:
    print('O Valor do Produto Com Juros Fica em: R${}'.format(d))
else:
    print('[ Valor Inválido ] \n Por Favor Digite Um Desses Números ( 1 , 2 , 3 ou 4 )')