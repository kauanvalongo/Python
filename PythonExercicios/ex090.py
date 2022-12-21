aluno = {}
situ = []
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a média do aluno: '))
if aluno['media'] < 6:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'
situ.append(aluno.copy())
print(f'O nome do aluno é {aluno["nome"]}')
print(f'A média do aluno é {aluno["media"]}')
print(f'A situação do aluno é {aluno["situacao"]}')
