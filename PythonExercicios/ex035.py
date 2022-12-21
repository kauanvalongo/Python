r1 = int(input('Valor da primeira reta:'))
r2 = int(input('Valor da segunda reta:'))
r3 = int(input('Valor da terceira reta:'))
if r3 < (r1 + r2) and r1 < (r2 + r3) and r2 < (r1 + r3):
    print('As retas PODEM formar um triângulo.')
else:
    print('As retas NÃO PODEM formar um triângulo!')



