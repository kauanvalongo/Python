n = int(input('Quantos Km/h estava o carro?'))
m = (n - 80) * 7
if n <= 80:
    print('Tudo certo!')
else:
    print('Você está acima da velocidade! Terá que pagar R${} de multa!'.format(m))


