ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    cont = str(input('Quer continuar? [S/N]: '))
    if cont in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    resp = int(input('Quer Saber a nota de qual aluno? (999 para parar)'))
    if resp == 999:
        break
    if resp <= len(ficha) - 1:
            print(f'Notas de {ficha[resp][0]} são {ficha[resp][1]}, por isso a média [{ficha[resp][2]}]')
print('<<< Volte Sempre! >>>')
