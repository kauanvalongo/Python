maior = homens = mulheres = 0
while True:
    idade = int(input('Qual a idade do candidato? '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Qual o sexo do candidato? [F/M]'))
    if idade >= 18:
        maior += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade >= 20:
        mulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja adicionar mais um candidato? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'No total foram cadastradas:\n{maior} Pessoas com mais de 18 anos\n{homens} Homens\n{mulheres} Mulheres com mais de 20 anos')
