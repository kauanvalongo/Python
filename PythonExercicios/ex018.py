import math
an = float(input('Digite o ângulo que deseja:'))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an,seno,math.ceil(seno)))
coseno = math.cos(math.radians(an))
print('O ângulo de {} tem o COSENO de {:.2f}'.format(an,coseno,math.ceil(coseno)))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an,tangente,math.ceil(tangente)))