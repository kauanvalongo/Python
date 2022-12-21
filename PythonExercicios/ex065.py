cont = 0
media = 0
maior = 0
menor = 0
s = 'S'
while s in 'Ss':
    num = int(input('Escolha um Número: '))
    media += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    s = (str(input('Quer Continuar? [S/N]')))
print(f'A Média dos numeros digitados é: {media / cont}')
print(f'O maior número digitado é: {maior}')
print(f'O menor número digitado é: {menor}')
