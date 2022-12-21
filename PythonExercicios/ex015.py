d = int(input('Quantos dias o carro foi alugado?'))
km = int(input('Quantos Km percorreu o carro durante esse período?'))
a = d*60
k = km*0.15
v = a+k
print('O valor total a pagar pelo aluguel é de R${}'.format(v))