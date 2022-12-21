import math
c1 = float(input('Qual o valor do cateto oposto?'))
c2 = float(input('Qual o valor do cateto adjacente?'))
v = (c1**2 + c2**2) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(v))

v2 = math.hypot(c1,c2)
print('Outro metodo para saber o valor da hypotenusa! {} '.format(v2))