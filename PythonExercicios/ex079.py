valores = []
while True:
    n = (int(input('Digite Um Valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor Adicionado...')
    else:
        print('O Valor Digitado Não Será Adicionado Pois é Repetido.')
    continuar = str(input('Quer Continuar?[S/N]'))
    if continuar in 'Nn':
        break
print('-='*30)
valores.sort()
print(f'Os Valores Digitados foram: {valores}')
