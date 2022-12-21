from datetime import date
data = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input(f'Digite o Ano de Nascimento das Pessoa {c}:'))
    idade = data - ano
    print(idade)
    if idade >= 18:
        print(f'Esta pessoa já é maior de idade.')
        maior += 1
    else:
        print('Esta pessoa ainda é menor de idade.')
        menor += 1
print(f'{maior} Pessoas São Maiores de Idade e {menor} Ainda São de Menor.')



