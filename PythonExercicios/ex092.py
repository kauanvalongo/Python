ficha = {}
ficha['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
ficha['idade'] = 2022 - ano
ctr = int(input('Carteira de trabalho: '))
if ctr != 0:
    ficha['contrato'] = int(input('Ano de Contratação: '))
    ficha['aposentadoria'] = ficha['contrato'] - ano + 35
    ficha['salario'] = float(input('Salário: '))
print('-='*30)
for k, v in ficha.items():
    print(f'- {k} tem valor: {v}')