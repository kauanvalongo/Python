lista = []
quant = 0
while True:
    n = int(input('Digite um valor aqui: '))
    lista.append(n)
    quant += 1
    cont = str(input('Deseja continuar? [S/N]'))
    if cont in 'Nn':
        break
print(f'Você digitou {quant} elementos')
lista.sort(reverse=True)
print(f'Os números digitados em ordem decrascente é: {lista}')
if 5 in lista:
    print(f'O Valor 5 foi digitado e está na lista.')
else:
    print('O valor 5 não foi digitado.')
