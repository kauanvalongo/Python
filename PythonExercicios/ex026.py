frase = str(input('Digite uma frase:')).strip().upper()
c = (frase.count('A'))
f = frase.find('A')
u = frase.rfind('A')
print('A letra A aparece {} vezes na frase.'.format(c))
print('A letra A aparece primeiro na casa {}.'.format(f))
print('A ultima letra A apareceu em {}'.format(u))

