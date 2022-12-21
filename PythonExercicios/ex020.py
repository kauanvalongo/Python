import random
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
n = [a1, a2, a3, a4]
random.shuffle(n)
print('A ordem de entrega dos trabalhos é:')
print(n)