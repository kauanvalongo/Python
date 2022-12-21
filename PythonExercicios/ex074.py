import random
cont = 0
maior = 0
menor = 0
while cont < 5:
    r = random.randint(0, 10)
    print(r,end='-')
    cont += 1
    if cont == 1:
        maior = r
        menor = r
    else:
        if r > maior:
            maior = r
        if r < menor:
            menor = r
print(f'FIM \nO Menor número foi {menor} \nE o maior foi número {maior}.')
