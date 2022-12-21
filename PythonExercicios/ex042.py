n1 = int(input('Escreva o tamanho da primeira reta:'))
n2 = int(input('Escreva o tamanho da segunda reta:'))
n3 = int(input('Escreva o tamanho da terceira reta:'))
if  n1 > (n2 + n3) or n2 > (n1 + n3) or n3 > (n1 + n2):
    print('[ ERRO ] \n Não é possível formar um triângulo com estas retas...')
elif n1 == n2 and n1 == n3 or n2 == n1 and n2 == n3 or n3 == n1 and n3 == n2:
    print('[ TRIÂNGULO EQUILÁTERO ]')
elif n1 == n2 or n3 == n1 or n3 == n2:
    print('[ TRIANGULO ISÓSCELES ]')
else:
    print('[ TRIÂNGULO ESCALENO ]')