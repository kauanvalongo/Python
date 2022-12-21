num = [[], [], [], [], [], [], [], [], []]
par = 0
impar = 0
maior2 = 0
soma3 = 0
for c in range(0, 9):
    n = int(input('Digite um número: '))
    num[c] = n
    if n % 2 == 0:
        par += n
    else:
        impar += n
    if c in (3,4,5):
        if n > maior2:
            maior2 = n
    if c in (2,5,8):
        soma3 += n
print('-='*30)
print(f'  [ {num[0]} ]',end = ' ')
print(f'  [ {num[1]} ]',end = ' ')
print(f'  [ {num[2]} ]')
print(f'  [ {num[3]} ]',end = ' ')
print(f'  [ {num[4]} ]',end = ' ')
print(f'  [ {num[5]} ]')
print(f'  [ {num[6]} ]',end = ' ')
print(f'  [ {num[7]} ]',end = ' ')
print(f'  [ {num[8]} ]')
print('-='*30)
print(f'A soma dos valores pares é: {par}')
print(f'A soma dos valores da terceira coluna é: {soma3}')
print(f'A soma dos valores ímpares é: {impar}')
print(f'O maior valor da segunda fileira é: {maior2}')
