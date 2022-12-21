print('=="=='* 20)
print('Calculador de Empréstimos..')
print('=="=='* 20)
valor = int(input('Digite o valor do empréstimo: R$'))
salario = int(input('Digite seu salário: R$'))
anos = int(input('Em quantos anos quer pagar?'))
x = salario * 30 / 100
y = valor / (anos * 12)
if y > x:
    print('Para pagar uma casa de {} em {} anos a prestação será de {:.2f}. \n EMPRÉSTIMO NEGADO'.format(valor,anos,y))
else:
    print('Para pagar uma casa de {} em {} anos a prestação será de {:.2f}. \n EMPRÉSTIMO ACEITO'.format(valor,anos,y))
