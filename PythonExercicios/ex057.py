s = str(input('Digite Seu Sexo: [ F/M ]')).strip().upper()[0]
while s not in 'MmFf':
      s = str(input('Dados Inválidos, Tente Novamente: [F/M]'))
print(f'Sexo registrado. {s}')
