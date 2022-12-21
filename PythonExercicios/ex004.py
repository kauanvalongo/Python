n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = (n1 + n2)
e = n1 ** n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
sub = n1 - n2
#ordem correta^ ()> ** > *,/,//>+,-
print('A soma é {}, o expoente é {}, a multiplicação é {}, a divisão é {:.3f}'.format(s,e,m,d),end='' )
print(' a divisão inteira é {} e a subtração é {}'.format(di,sub))

print('A soma é {}, o expoente é {},\n a multiplicação é {},\n a divisão é {:.3f}'.format(s,e,m,d) )
print(' a divisão inteira é {} e a subtração é {}'.format(di,sub))
