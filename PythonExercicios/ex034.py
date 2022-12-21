salario = int(input('Digite o seu salário para saber quanto será o aumento: R$'))
if salario >= 1251:
    novo = salario + (salario *10 / 100)
if salario <= 1250:
    novo = salario = + (15//100)
print('Seu novo salário será de R${}!'.format(novo))
