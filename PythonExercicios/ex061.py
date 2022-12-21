n1 = int(input('Termo:'))
n2 = int(input('Razão:'))
a = n1
p = 1
while p <= 10:
    print(f'{a}', end='-')
    a += n2
    p += 1
print('Fim')
