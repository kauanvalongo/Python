n1 = float(input('Escreva sua nota na prova:'))
n2 = float(input('Escreva sua nota no teste:'))
n = (n1 + n2) / 2
if n >= 6.0:
    print('Sua nota foi {}. Parabéns, você foi aprovado!'.format(n))
elif n <= 5.9:
    print('Sua nota foi {}. Você ficou de recuperação.'.format(n))
elif n < 5.0:
    print('Sua nota foi {}. Você foi reprovado.'.format(n))