num = []
maior = menor = 0
for c in range(0,5):
    num.append(int(input(f'Digite o valor {c}:')))
    if c == 0:
        maior = num[c]
        menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print(f'você digitou os Valores: {num}')
print(f'O maior valor digitado foi: {maior} nas posições: ',end='')
for v, i in enumerate(num):
    if i == maior:
        print(f'{v}..',end='')
print(f'\nO menor valor digitado foi: {menor} nas posições :',end='')
for v, i in enumerate(num):
    if i == menor:
        print(f'{v}... ', end='')
