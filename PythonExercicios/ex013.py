s = int(input('Digite seu salário atual: R$'))
a = int(input('Qual a porcentagem do aumento no salário?'))
t = s + (s*a/100)
print('Seu novo salario é de R${}'.format(t))